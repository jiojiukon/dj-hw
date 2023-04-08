from django.contrib import admin
from .models import Phone

@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ['name','price','image','release_date', 'slug','lte_exists']
    prepopulated_fields = {'slug': ('name',)}

# Register your models here.
