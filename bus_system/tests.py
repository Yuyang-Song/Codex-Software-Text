"""Basic tests for the bus management system.

These unit tests ensure core models and views behave as expected. They are
derived from the features outlined in the PDF document.
"""

from django.test import TestCase
from django.urls import reverse
from .models import User, Vehicle, Booking

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
        self.booking = Booking.objects.create(
            user=self.user,
            pickup_location='校区A',
            destination='校区B',
            scheduled_time='2025-06-15 08:00:00'
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
