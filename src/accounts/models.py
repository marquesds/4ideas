from django.db import models
from django.contrib.auth.models import User

class Player(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name or self.user.username

    class Meta:
        verbose_name = 'Player'
        verbose_name_plural = 'Players'
