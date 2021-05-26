from django.test import TestCase
from django.db import IntegrityError
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def setUp(self):
        self.email_1 = 'test@erischon.dev'
        self.email_2 = 'tesT@erischON.DEV'
        self.password = 'azerty12345'

    def test_create_user_with_email_successful(self):
        """ Test creating a new user with an email is successful. """
        user = get_user_model().objects.create_user(
            email=self.email_1,
            password=self.password,
        )

        self.assertEqual(user.email, self.email_1)
        self.assertTrue(user.check_password(self.password))

    def test_new_user_email_normalized(self):
        """ Test the email for a new user is normalized. """
        with self.assertRaises(IntegrityError):
            get_user_model().objects.create_user(self.email_1, self.password)
            get_user_model().objects.create_user(self.email_2, self.password)

    def test_new_user_invalid_email(self):
        """ Test creating user with no email raises error. """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, self.password)

    def test_create_new_superuser(self):
        """ Test creating a new superuser. """
        user = get_user_model().objects.create_superuser(
            self.email_1,
            self.password
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
