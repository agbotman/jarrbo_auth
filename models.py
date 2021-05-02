from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.core.mail import send_mail
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

class MyUserManager(BaseUserManager):
    """
    A manager that is used with custom User model defined below 
    It overrides the _create_user and create_superuser methods
    so that email is required and unique
    """
    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    """
    A customer User model, the User is uniquely defined by its email address https://docs.djangoproject.com/en/1.10/topics/auth/customizing/#substituting-a-custom-user-model
    No username field and email field is required and unique
    """
    email = models.EmailField(unique=True, null=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    # A string describing the name of the field on the user model that is used as the unique identifier
    # must be set and is used by several API's
    USERNAME_FIELD = 'email'

    # Override the default manager to MyUserManager defined above
    objects = MyUserManager()

    def __str__(self):
        return self.email

    # get_full_name and get_short_name must be overridden 
    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    # This method must be defined again because we inheret from AbstractBaseUser
    # and it is defined in AbstractUser
    def email_user(self, subject, message, from_email, **kwargs):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, settings.EMAIL_HOST_USER, [self.email], **kwargs)
