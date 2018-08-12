from django.contrib import admin
from .models import Personalized,PersonalizedTour


class PersonalizedAdmin(admin.ModelAdmin):
    list_display = ['title','LastName']

class PersonalizedTourAdmin(admin.ModelAdmin):
    list_display = ['City', 'Price', 'title', 'confirm','Tourtype']

admin.site.register(Personalized, PersonalizedAdmin)
admin.site.register(PersonalizedTour, PersonalizedTourAdmin)