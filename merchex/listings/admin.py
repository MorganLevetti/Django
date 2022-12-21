from django.contrib import admin
from listings.models import Band
from listings.models import Product


class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'year_formed', 'genre', 'biography')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'type', 'band')


admin.site.register(Band, BandAdmin)
admin.site.register(Product, ProductAdmin)
