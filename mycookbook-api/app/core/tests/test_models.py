from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def setUp(self):
        self.email = 'test@erischon.dev'
        self.password = 'azerty12345'

    def test_create_user_with_email_successful(self):
        """ Test creating a new user with an email is successful. """
        user = get_user_model().objects.create_user(
            email=self.email,
            password=self.password,
        )

        self.assertEqual(user.email, self.email)
        self.assertTrue(user.check_password(self.password))
