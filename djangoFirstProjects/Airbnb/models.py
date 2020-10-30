from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.admin import admin
from django.utils import timezone
from django.contrib.admin.models import LogEntry, ADDITION
from django.contrib.contenttypes.models import ContentType
from django.core.validators import MinValueValidator


# Create your models here.


class City(models.Model):
    name = models.CharField(max_length=50, default="No name provided")

    def __str__(self):
        return "This is the city: " + self.name


class Property(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.PROTECT)
    tittle = models.CharField(max_length=60)
    description = models.CharField(max_length=500)
    pricePerDay = models.FloatField(default=0.0, validators=[MinValueValidator(0.0)])
    maxPeople = models.IntegerField(validators=[MinValueValidator(0.0)])
    photo = models.ImageField(upload_to="gallery")

    def __str__(self):
        return self.tittle


class Reservation(models.Model):
    property = models.ForeignKey(Property, on_delete=models.PROTECT)
    date = models.DateField(default=timezone.now())
    code = models.CharField(max_length=70, default=str(timezone.now()))
    subtotal = models.FloatField(default=0.0)
    commission = models.FloatField(default=0.0)
    total = models.FloatField(default=0.0)
    guestName = models.CharField(max_length=50)
    guestLastName = models.CharField(max_length=50)
    guestEmail = models.EmailField()

    def __str__(self):
        return self.code


class DateRental(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name="dates")
    reservation = models.ForeignKey(Reservation, null=True, blank=True, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.date)


class DateRentalInline(admin.TabularInline):
    model = DateRental
    fk_name = "property"
    max_num = 7


class PropertyAdmin(admin.ModelAdmin):
    fields = ('city', 'tittle', 'description', 'pricePerDay', 'maxPeople', 'photo')
    inlines = [DateRentalInline, ]

    def get_queryset(self, request):
        qs = super(PropertyAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        property_ct = ContentType.objects.get_for_model(Property)
        log_entries = LogEntry.objects.filter(
            content_type=property_ct,
            user=request.user,
            action_flag=ADDITION
        )
        user_property_ids = [a.object_id for a in log_entries]
        return qs.filter(id__in=user_property_ids)

    def save_model(self, request, instance, form, change):
        instance.owner = request.user
        super(PropertyAdmin, self).save_model(request, instance, form, change)
