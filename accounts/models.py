from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.db import models

# Create your models here.
class MyUserManager(BaseUserManager):
    def create_user(self, email, password, nickName,):
        if not email:
            raise ValueError('Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, nickName=nickName,)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, email, password, nickName,):
        user = self.create_user(email=email, password=password, nickName=nickName,)
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, null=True)
    nickName = models.CharField(max_length=30, blank=True, default='')
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nickName']
    objects = MyUserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.nickName

    def set_username(self,username):
        self.nickName = username

    @property
    def is_staff(self):
        return self.is_admin
