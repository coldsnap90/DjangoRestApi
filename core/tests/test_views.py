from django.test import TestCase
from django.urls import reverse

from core.models import Student

class AuthorListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 13 authors for pagination tests
        number_of_students = 13

        for student_id in range(number_of_students):
            Student.objects.create(
                first_name=f'First_Name {student_id}',
                last_name=f'Surname {student_id}',
            )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/api/student/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('students'))
        self.assertEqual(response.status_code, 200)




