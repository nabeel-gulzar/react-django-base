import datetime

from django.test import TestCase
from .models import Person


class PersonModelTest(TestCase):

    def test_full_name_is_first_space_last(self):
        person = Person(
            identification_no='sdf1234',
            first_name='first',
            last_name='last',
            dob=datetime.date(1999, 5, 3)
        )
        self.assertEqual(str(person), f"{person.first_name} {person.last_name}")
