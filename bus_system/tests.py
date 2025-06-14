"""Basic tests for the bus management system.

These unit tests ensure core models and views behave as expected. They are
derived from the features outlined in the PDF document.
"""

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from .models import User, Vehicle, Booking, Dispatch, Driver

class BusSystemTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123',
            phone='13800138000'
        )
        self.vehicle = Vehicle.objects.create(
            plate_number='京A12345',
            model='大型客车',
            capacity=45,
            status='A',
            last_maintenance='2025-06-01'
        )
        aware_time = timezone.make_aware(timezone.datetime(2025, 6, 15, 8, 0))
        self.booking = Booking.objects.create(
            user=self.user,
            pickup_location='校区A',
            destination='校区B',
            scheduled_time=aware_time
        )

        # 为实时监控视图准备一个调度记录
        driver_user = User.objects.create_user(
            username='driver1',
            password='driverpass',
            phone='13900139000'
        )
        driver = Driver.objects.create(
            user=driver_user,
            license_number='A1234567',
            hire_date='2024-01-01'
        )
        self.dispatch = Dispatch.objects.create(
            booking=self.booking,
            driver=driver,
            vehicle=self.vehicle
        )

    def test_vehicle_creation(self):
        self.assertEqual(self.vehicle.plate_number, '京A12345')
        self.assertEqual(self.vehicle.capacity, 45)

    def test_booking_creation(self):
        self.assertEqual(self.booking.status, 'P')
        self.assertEqual(self.booking.user.username, 'testuser')

    def test_realtime_monitor_view(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('realtime-monitor'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "实时车辆监控")

    def test_update_location_endpoint(self):
        """POST 经纬度数据后应在数据库中保存记录"""
        self.client.login(username='testuser', password='testpass123')
        url = reverse('update-location', args=[self.dispatch.id])
        payload = {
            'latitude': 39.9,
            'longitude': 116.4
        }
        response = self.client.post(url, payload, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        from .models import LocationHistory
        count = LocationHistory.objects.filter(dispatch=self.dispatch).count()
        self.assertEqual(count, 1)
