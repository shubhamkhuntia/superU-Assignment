from django.test import TestCase
from home.models import UserProfile


class UserProfileModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create test data before running the tests
        UserProfile.objects.create(
            name='John Doe',
            email='johndoe@example.com',
            bio='Lorem ipsum dolor sit amet',
            profile_picture='path/to/profile_picture.jpg'
        )

    def test_create_user_profile(self):
        # Retrieve the created user profile from the database
        user_profile = UserProfile.objects.get(email='johndoe@example.com')

        # Perform assertions to check if the created user profile matches the provided data
        self.assertEqual(user_profile.name, 'John Doe')
        self.assertEqual(user_profile.email, 'johndoe@example.com')
        self.assertEqual(user_profile.bio, 'Lorem ipsum dolor sit amet')
        self.assertEqual(user_profile.profile_picture,
                         'path/to/profile_picture.jpg')
