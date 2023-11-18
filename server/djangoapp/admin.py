from django.contrib import admin
from .models import CarMake, CarModel


# Register your models here.

class CarModelInline(admin.TabularInline): 
    model = CarModel
    extra = 1 

class CarModelAdmin(admin.ModelAdmin):
    list_display = ('car_make', 'name', 'type', 'year', 'dealer_id')
    list_filter = ('car_make', 'type', 'year')
    search_fields = ('name', 'car_make__name', 'dealer_id')

class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]
    list_display = ('name', 'description')
    search_fields = ('name',)

# Register models here
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
