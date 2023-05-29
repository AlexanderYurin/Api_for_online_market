from django.contrib import admin
from .models import Profile


# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_filter = ('first_name',)
    list_display = ('id', 'first_name', 'last_name', 'date_registration')


admin.site.register(Profile, ProfileAdmin)
