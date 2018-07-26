from django.contrib import admin
from .models import City, Post, Country, Language, TypeOfTour, SNS, Booking
from .forms import BookMForm
class PostAdmin(admin.ModelAdmin):
    list_display = ['City', 'Price', 'title', 'representation', 'confirm','Tourtype']

class LaguageAdmin(admin.ModelAdmin):
    list_display = ['language']

class TypeOfTourAdmin(admin.ModelAdmin):
    list_display = ['type']

class CountryAdmin(admin.ModelAdmin):
    list_display = ['name']
    form = BookMForm

class CityAdmin(admin.ModelAdmin):
    list_display = ['city']

admin.site.register(Country, CountryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Language, LaguageAdmin)
admin.site.register(TypeOfTour, TypeOfTourAdmin)
admin.site.register(City, CityAdmin)

class BookingAdmin(admin.ModelAdmin):
    list_display = ['LastName']

class SNSAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(SNS,SNSAdmin)
admin.site.register(Booking,BookingAdmin)