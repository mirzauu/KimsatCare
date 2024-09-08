from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import RegexValidator, validate_email
from django.utils.translation import gettext_lazy as _

# Phone number validator
phone_regex = RegexValidator(regex=r"^\d{10}$", message="Phone number must be 10 digits.")

# Custom User Manager
class CustomUserManager(BaseUserManager):
    def create_user(self, email, phone_number, password=None, **extra_fields):
        if not email:
            raise ValueError(_('The Email field must be set'))
        if not phone_number:
            raise ValueError(_('The Phone number field must be set'))

        email = self.normalize_email(email)
        user = self.model(email=email, phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, phone_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, phone_number, password, **extra_fields)

# Patient model
class Patient(AbstractBaseUser):
    phone_number = models.CharField(max_length=10, unique=True, validators=[phone_regex])
    is_active = models.BooleanField(default=True)
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.phone_number

# Custom User model
class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True, blank=True, null=True, validators=[validate_email])
    phone_number = models.CharField(max_length=10, unique=True, blank=True, null=True, validators=[phone_regex])
    password = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

# Role model
class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

# UserRole model
class UserRole(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'role')

    def __str__(self):
        return f"{self.user.email} - {self.role.name}"
