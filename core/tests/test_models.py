from django.test import TestCase

from core.models import Student

class StudentModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Student.objects.create(first_name='Frank', last_name='Shamrock')

    def test_first_name_label(self):
        Student = Student.objects.get(id=1)
        field_label = Student._meta.get_field('first_name').verbose_name
        self.assertEqual(field_label, 'first name')

    def test_date_of_death_label(self):
        Student = Student.objects.get(id=1)
        field_label = Student._meta.get_field('is_staff').verbose_name
        self.assertEqual(field_label, False)

    def test_first_name_max_length(self):
        Student = Student.objects.get(id=1)
        max_length = Student._meta.get_field('first_name').max_length
        self.assertEqual(max_length, 100)


    def test_get_absolute_url(self):
        Student = Student.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEqual(Student.get_absolute_url(), '/api/student/1')