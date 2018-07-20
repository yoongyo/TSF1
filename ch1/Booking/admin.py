from django.contrib import admin
from .models import Booking
from .forms import BookMForm

class BookingAdmin(admin.ModelAdmin):
    form = BookMForm


admin.site.register(Booking,BookingAdmin)