from django.contrib import admin
from .models import Review

class ReviewAdmin(admin.ModelAdmin):
    list_display = ['post','booking']

admin.site.register(Review, ReviewAdmin)