from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin, UserManager)
from django.conf import settings
from django.core import validators
import re

GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)

# Default images
DEFAULT_PROFILE_IMAGE = settings.STATIC_URL + '4ideas/img/default.png'
DEFAULT_COVER_IMAGE = settings.STATIC_URL + '4ideas/img/cover.jpeg'

class Player(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=200)
    username = models.CharField(
        'Username', max_length=30, unique=True,
        validators=[
            validators.RegexValidator(re.compile('^[\w.+-]+$'),
            'Username can only contain letters, digits or the following characters: ./+/-/_',
            'invalid')
        ]
    )
    email = models.EmailField('Email', max_length=150, unique=True)
    bio = models.TextField('Bio', max_length=5000, blank=True, null=True)
    gender = models.CharField(max_length=6, blank=True, null=True, choices=GENDER_CHOICES)
    birth_date = models.DateField('Birth Date', blank=True, null=True)

    profile_image = models.CharField(max_length=300, default=DEFAULT_PROFILE_IMAGE)
    cover_image = models.CharField(max_length=300, default=DEFAULT_COVER_IMAGE)

    # Setting up AbstractBaseUser
    is_active = models.BooleanField('Is active?', blank=True, default=True)
    is_staff = models.BooleanField('Is admin?', blank=True, default=False)

    date_joined = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return self.name

    def __str__(self):
        return self.name or self.username

    class Meta:
        verbose_name = 'Player'
        verbose_name_plural = 'Players'


class Friend(models.Model):
    # Many-to-one relationship. More at:
    # https://docs.djangoproject.com/en/1.8/topics/db/examples/many_to_one/
    player = models.ForeignKey(Player)

    def __str__(self):
        return self.player.name or self.player.username

    class Meta:
        verbose_name = 'Friend'
        verbose_name_plural = 'Friends'
