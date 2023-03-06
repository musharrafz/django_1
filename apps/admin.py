from django.contrib import admin
from django.contrib.auth.models import User
from .models import Product ,Region, District



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    fields = ('name',)


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    fields = ('name',)


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ('id','name','region_id')
    fields = ('name',)