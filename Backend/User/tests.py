from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Role, UserProfile, UserRole

class UserModelTest(TestCase):
    def test_create_user(self):
        user = get_user_model().objects.create_user(
            username='testuser',
            email='test@example.com',
            password='password123'
        )
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'test@example.com')
        self.assertTrue(user.check_password('password123'))

    def test_create_superuser(self):
        user = get_user_model().objects.create_superuser(
            username='adminuser',
            email='admin@example.com',
            password='password123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_create_role(self):
        role = Role.objects.create(name='Doctor')
        self.assertEqual(role.name, 'Doctor')

    def test_assign_role(self):
        user = get_user_model().objects.create_user(
            username='testuser',
            email='test@example.com',
            password='password123'
        )
        role = Role.objects.create(name='Doctor')
        user_role = UserRole.objects.create(user=user, role=role)
        self.assertEqual(user_role.user.username, 'testuser')
        self.assertEqual(user_role.role.name, 'Doctor')
