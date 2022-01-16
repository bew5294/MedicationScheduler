from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from phonenumber_field.modelfields import PhoneNumberField

'''
useful links: 
1) https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html
2) https://simpleisbetterthancomplex.com/article/2021/07/08/what-you-should-know-about-the-django-user-model.html
3) PhoneNumberField: https://github.com/stefanfoulis/django-phonenumber-field
'''


class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, password=None):
        if not email:
            raise ValueError("User must have an email address")
        if not username:
            raise ValueError("User must have an username")
        if not first_name:
            raise ValueError("User must have a first name")
        if not last_name:
            raise ValueError("User must have a last name")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password, first_name, last_name):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)
        return user


# Create your models here.
class Account(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name="date_joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last_login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]

    objects = MyAccountManager()

    # required method. Can be changed if users have different permissions
    def has_perm(self, perm, obj=None):
        return self.is_admin

    # required method. TODO: read about it
    def has_module_perms(self, app_label):
        return True


class Profile(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    # TODO: read about formating for phone number field
    phone_number = models.CharField(max_length=16, blank=True, null=True)
    dob = models.DateField(max_length=8, blank=True, null=True)
    primary_physician = models.CharField(max_length=200, null=True, blank=True)
    preferred_pharmacy = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.user.username
