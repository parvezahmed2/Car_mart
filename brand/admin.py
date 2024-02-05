from django.contrib import admin
from . import models
# Register your models here.
 

class ModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',)}
    lsit_display = ['name', 'slug']
admin.site.register(models.CarModel, ModelAdmin)