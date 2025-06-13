"""Management command to bootstrap example data.

The demo data helps illustrate the workflow described in the PDF by creating
users, drivers and vehicles that can be used during development.
"""

from django.core.management.base import BaseCommand
from django.utils import timezone
from bus_system.models import User, Driver, Vehicle

class Command(BaseCommand):
    help = 'Initialize sample data for the bus system'
    
    def handle(self, *args, **options):
        # 创建管理员
        admin_user = User.objects.create_superuser(
            username='admin',
            password='admin123',
            phone='13800000000'
        )
        
        # 创建普通用户
        for i in range(1, 6):
            user = User.objects.create_user(
                username=f'user{i}',
                password=f'pass{i}',
                phone=f'1380000000{i}'
            )
        
        # 创建司机
        for i in range(1, 4):
            driver_user = User.objects.create_user(
                username=f'driver{i}',
                password=f'driver{i}',
                phone=f'1390000000{i}'
            )
            Driver.objects.create(
                user=driver_user,
                license_number=f'DRIVER{i}123456',
                hire_date=timezone.now().date(),
            )
        
        # 创建车辆
        vehicles = [
            {'plate': '京A12345', 'model': '大型客车', 'capacity': 45},
            {'plate': '京B67890', 'model': '中型客车', 'capacity': 30},
            {'plate': '京C54321', 'model': '小型巴士', 'capacity': 20},
        ]
        for v in vehicles:
            Vehicle.objects.create(
                plate_number=v['plate'],
                model=v['model'],
                capacity=v['capacity'],
                last_maintenance=timezone.now().date()
            )
        
        self.stdout.write(self.style.SUCCESS('Successfully initialized sample data'))
