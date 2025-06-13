"""Database models for the school bus management system.

These models follow the project description in the accompanying PDF. The
specification mentions modules such as user management, driver management,
vehicle scheduling and historical tracking. Each class below represents one
of these modules.
"""

from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """System user with an additional phone field and credit rating."""
    CREDIT_CHOICES = [
        ('A', '优秀'),
        ('B', '良好'),
        ('C', '一般'),
        ('D', '较差'),
    ]
    phone = models.CharField(max_length=15, unique=True)
    credit_rating = models.CharField(max_length=1, choices=CREDIT_CHOICES, default='B')
    
    def __str__(self):
        return self.username

class Driver(models.Model):
    """Model representing a bus driver."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=20)
    hire_date = models.DateField()
    
    def __str__(self):
        return self.user.username

class Vehicle(models.Model):
    """Information about each vehicle in the fleet."""
    STATUS_CHOICES = [
        ('A', '可用'),
        ('M', '维护中'),
        ('D', '已调度'),
    ]
    plate_number = models.CharField(max_length=10, unique=True)
    model = models.CharField(max_length=20)
    capacity = models.IntegerField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='A')
    last_maintenance = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.plate_number

class Booking(models.Model):
    """A passenger reservation for a specific trip."""
    STATUS_CHOICES = [
        ('P', '待处理'),
        ('C', '已确认'),
        ('X', '已取消'),
        ('D', '已完成'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pickup_location = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    scheduled_time = models.DateTimeField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user} - {self.scheduled_time}"

class Dispatch(models.Model):
    """Assignment of a driver and vehicle to a booking."""
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    dispatch_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"调度#{self.id}"

class LocationHistory(models.Model):
    """Historical GPS points for a dispatch, used for tracking."""
    dispatch = models.ForeignKey(Dispatch, on_delete=models.CASCADE)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "位置历史记录"
