from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

class User(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=255,unique=True, error_messages={
        'unique': _("A user with that email already exist.")})
    phone_number = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    nationality = models.CharField(max_length=50)
    is_active = models.BooleanField(_('Active'), default=True)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name','phone_number','date_of_birth','nationality']
