from django.contrib import admin
from .models import City, Post, Language, TypeOfTour, SNS, Booking, Time, Duration
from .forms import BookMForm, PostMForm



class PostAdmin(admin.ModelAdmin):
    list_display = ['City', 'Price', 'title', 'representation', 'confirm','Tourtype']

class LaguageAdmin(admin.ModelAdmin):
    list_display = ['language']

class TypeOfTourAdmin(admin.ModelAdmin):
    list_display = ['type']

class CityAdmin(admin.ModelAdmin):
    list_display = ['city']

class TimeAdmin(admin.ModelAdmin):
    list_display = ['time']

class DurationAdmin(admin.ModelAdmin):
    list_display = ['duration']

admin.site.register(Post, PostAdmin)
admin.site.register(Language, LaguageAdmin)
admin.site.register(TypeOfTour, TypeOfTourAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Time,TimeAdmin)
admin.site.register(Duration,DurationAdmin)


class BookingAdmin(admin.ModelAdmin):
    list_display = ['LastName']

class SNSAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(SNS,SNSAdmin)
admin.site.register(Booking,BookingAdmin)