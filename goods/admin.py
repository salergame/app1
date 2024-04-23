from django.contrib import admin

<<<<<<< HEAD
from goods.models import Categories, Filter_test, Products

# admin.site.register(Categories)
# admin.site.register(Products)
@admin.register(Filter_test)
class Filter_testAdmin(admin.ModelAdmin):
        raw_id_fields=['product']


=======
from goods.models import Categories, Products
# Register your models here.

# admin.site.register(Categories)
# admin.site.register(Products)
>>>>>>> 7203c0d3ca24d97ad35e4406b64f3838b5a5f355

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
<<<<<<< HEAD
    list_display = ["name",]

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ["name","quantity","price","discount"]
    list_editable = ["discount",'quantity']
    search_fields = ["name","description"]
    list_filter = ["discount","quantity","category"]
    fields = [
        "name",
        "category",
        "slug",
        "description",
        "image",
        ("price","discount"),
        "quantity",
    ]
    
=======

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
>>>>>>> 7203c0d3ca24d97ad35e4406b64f3838b5a5f355
