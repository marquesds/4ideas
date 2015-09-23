from django.db import models
from accounts.models import Player
from django.core.exceptions import ValidationError
import re

class Post(models.Model):
    content = models.TextField(max_length=10000)
    player = models.ForeignKey(Player)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # If post's content has only space and carriage return characters
    # do not post.
    def clean(self):
        if re.match(r"^[\n\r\s]+$", self.content):
            raise ValidationError('Content not valid.')

    def __str__(self):
        return self.content

    class Meta:
        ordering = ['-created_at']
