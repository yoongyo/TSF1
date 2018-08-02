from django.contrib import admin
from .models import Personalized


class PersonalizedAdmin(admin.ModelAdmin):
    pass

admin.site.register(Personalized, PersonalizedAdmin)