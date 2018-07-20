from django.contrib import admin
from .models import Profile,Language
from .forms import ProfileMForm


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user']

admin.site.register(Language)