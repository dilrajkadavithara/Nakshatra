from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

from nisapp.models import District, LocalArea, Lead

class DistrictListTestCase(TestCase):
    def setUp(self):
        # Load your test data here, ensuring it happens BEFORE the test runs
        District.objects.create(district_id='KER01', district_name='Thiruvananthapuram', state_name='KERALA')
        District.objects.create(district_id='KER02', district_name='Kollam', state_name='KERALA')

        self.client = APIClient()

    def test_get_districts(self):
        response = self.client.get('/api/districts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check if two districts are returned
        self.assertEqual(len(response.data), 2) 

        # Updated assertions to exclude 'state_name'
        expected_data = [
            {'district_id': 'KER01', 'district_name': 'Thiruvananthapuram'},
            {'district_id': 'KER02', 'district_name': 'Kollam'},
        ]
        self.assertEqual(response.data, expected_data)

class LocalAreaListTestCase(TestCase):
    def setUp(self):
        self.district = District.objects.create(district_id='KER01', district_name='Thiruvananthapuram', state_name='KERALA')
        LocalArea.objects.create(local_area_id='TVPM01', local_area_name='Kowdiar', district=self.district)
        self.client = APIClient()

    def test_get_local_areas_with_district_id(self):
        response = self.client.get(f'/api/local-areas/?district_id={self.district.district_id}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

        # Optionally, add more specific assertions about the response data

class LeadCreateTestCase(TestCase):
    def setUp(self):
        self.district = District.objects.create(district_id='KER01', district_name='Thiruvananthapuram', state_name='KERALA')
        # Explicitly create a LocalArea associated with the district
        self.local_area = LocalArea.objects.create(local_area_id='TVPM01', local_area_name='Kowdiar', district=self.district)
        self.client = APIClient()

    def test_create_valid_lead(self):
        data = {
            'name': 'John Doe',
            'phone_number': '1234567890',
            'email': 'john@example.com',
            'district': self.district.district_id,
            'local_area': self.local_area.local_area_id,  # Reference the existing local_area
            # ... other lead fields
        }

        response = self.client.post('/api/leads/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Optionally, add assertions to check the created lead data in the response