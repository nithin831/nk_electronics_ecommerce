from django.contrib import admin
from  .models import *
# Register your models here.
class ImagesTublerinline(admin.TabularInline):
    model = Images

class TagTublerinline(admin.TabularInline):
    model = Tag
    
class ProductAdmin(admin.ModelAdmin):
    inlines = [ImagesTublerinline, TagTublerinline]
    
    
class Order_itemTublerinline(admin.TabularInline):
    model = Order_item
    
class OrderAdmin(admin.ModelAdmin):
    inlines = [Order_itemTublerinline]
    list_display = ['firstname','phone','email', 'payment_id', 'paid', 'date']
    search_fields = ['firstname','email', 'payment_id']
       
admin.site.register(Category)

admin.site.register(Brand)

admin.site.register(Color)

admin.site.register(Filter_price)

admin.site.register(Product, ProductAdmin)

admin.site.register(Images)

admin.site.register(Tag)

admin.site.register(Contact_us)

admin.site.register(Order, OrderAdmin)

admin.site.register(Order_item)

