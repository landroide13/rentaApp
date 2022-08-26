from django.contrib import admin
from .models import Car, Client

# Register your models here.

admin.site.site_header = "Rental App Admin"
admin.site.site_title = "Rental Car"
admin.site.index_title = "Welcome to the Rental App Admin Area"


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    fields = ['brand', 'model', 'color', 'plate']
    list_display = ['brand', 'model', 'plate']
    list_filter= ['brand']
    search_fields = ['brand']

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    fields = ['first_name', 'last_name', 'email']
    list_display = ['id','first_name', 'last_name']
    search_fields = ['first_name']






