from django.contrib import admin

from deliver.models import Order, Box,  Good


# Register your models here.

@admin.register(Order)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(Box)
class AuthorAdmin(admin.ModelAdmin):
    pass



@admin.register(Good)
class AuthorAdmin(admin.ModelAdmin):
    pass