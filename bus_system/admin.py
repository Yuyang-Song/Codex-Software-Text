from django.contrib import admin
from .models import User, Driver, Vehicle, Booking, Dispatch, LocationHistory

class UserAdmin(admin.ModelAdmin):
    search_fields = ['username', 'phone']  # 添加搜索字段

class DriverAdmin(admin.ModelAdmin):
    search_fields = ['user__username', 'license_number']  # 添加搜索字段

class VehicleAdmin(admin.ModelAdmin):
    list_display = ('plate_number', 'model', 'capacity', 'status')
    list_editable = ('status',)
    search_fields = ['plate_number', 'model']  # 添加搜索字段

class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'pickup_location', 'destination', 'scheduled_time', 'status')
    list_filter = ('status', 'scheduled_time')
    search_fields = ['user__username', 'pickup_location']  # 添加搜索字段

class DispatchAdmin(admin.ModelAdmin):
    list_display = ('booking', 'driver', 'vehicle', 'dispatch_time')
    autocomplete_fields = ('booking', 'driver', 'vehicle')  # 现在可以安全使用
    # 添加搜索字段
    search_fields = [
        'booking__user__username', 
        'driver__user__username', 
        'vehicle__plate_number'
    ]

admin.site.register(User, UserAdmin)  # 注册时使用自定义Admin
admin.site.register(Driver, DriverAdmin)  # 注册时使用自定义Admin
admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(Booking, BookingAdmin)
admin.site.register(Dispatch, DispatchAdmin)

admin.site.register(LocationHistory)
