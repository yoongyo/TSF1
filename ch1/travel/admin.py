from django.contrib import admin
from .models import City, Post, Country, Language, TypeOfTour

class PostAdmin(admin.ModelAdmin):
    list_display = ['City', 'Price', 'title']

class LaguageAdmin(admin.ModelAdmin):
    list_display = ['language']

class TypeOfTourAdmin(admin.ModelAdmin):
    list_display = ['type']

class CountryAdmin(admin.ModelAdmin):
    list_display = ['country']

class CityAdmin(admin.ModelAdmin):
    list_display = ['city']

admin.site.register(Country, CountryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Language, LaguageAdmin)
admin.site.register(TypeOfTour, TypeOfTourAdmin)
admin.site.register(City, CityAdmin)