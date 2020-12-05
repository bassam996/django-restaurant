from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(BreakFast)
admin.site.register(Lunch)
admin.site.register(Dinner)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ['ordered_at']
    list_filter  = ['ordered_at']


admin.site.register(Orders , OrdersAdmin)
