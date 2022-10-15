from django.contrib import admin
from .models import Hotel_rooms

@admin.register(Hotel_rooms)
class hotel_register(admin.ModelAdmin):
    list_display = ['title']

