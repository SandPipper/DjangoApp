from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from foodtaskerapp.models import Restaurant, Customer, Driver, Meal, Order, OrderDetails


@admin.register(OrderDetails)
class OrderDetailsAdmin(admin.ModelAdmin):
    fields = (('order', 'meal'), ('quantity', 'sub_total__gte')) #TODO find sub_totals more then 120$
    list_display = ('id', 'quantity', 'sub_total')
    search_fields = ('id', 'meal__name', 'sub_total')

class OrderDetailsInline(admin.TabularInline):
    model = OrderDetails
    extra = 0


# @admin.register(Restaurant, Customer, Driver, Meal, Order, OrderDetails)
#



admin.site.register(Restaurant)
admin.site.register(Customer)
admin.site.register(Driver)
admin.site.register(Meal)
admin.site.register(Order)
# admin.site.register(OrderDetails)
