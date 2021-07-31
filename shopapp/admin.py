from django.contrib import admin
from shopapp.models import Category, Product, BussinesData, Promo

def publicar(modeladmin, request, queryset):
    queryset.update(estado='Publicado')

class ProductDisplay(admin.ModelAdmin):
    list_display = ['name', 'category', 'estado']
    list_filter = ('name', 'estado')
    ordering = ['name']
    actions = [publicar]

class CategoryDisplay(admin.ModelAdmin):
    list_display = ['name', 'slug']
    list_filter = ('name', 'slug')
    ordering = ['name']


# Register your models here.
admin.site.register(Category, CategoryDisplay)
admin.site.register(Product, ProductDisplay)
admin.site.register(BussinesData)
admin.site.register(Promo)