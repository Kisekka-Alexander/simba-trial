from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

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
