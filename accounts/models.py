from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        '''
        Create a CustomUser with email, name, password and other extra fields
        '''
        if not email:
            raise ValueError('The email is required to create this user')
        email = CustomUserManager.normalize_email(email)
        cuser = self.model(email=email, is_active=True, is_admin=False,
                )
        cuser.set_password(password)
        cuser.save(using=self._db)
        return cuser

    def create_superuser(self, email, password=None):
        u = self.create_user(email, password)
        u.is_active = True
        u.is_admin = True
        u.save(using=self._db)
        return u

class User(AbstractBaseUser):
    """
    Custom user class.
    """
    email = models.EmailField('email address', unique=True, db_index=True)
    joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    ip = models.CharField(max_length=39)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'

    def __unicode__(self):
        return self.email
