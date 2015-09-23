# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.auth.models
import re
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(help_text='Designates that this user has all permissions without explicitly assigning them.', default=False, verbose_name='superuser status')),
                ('name', models.CharField(max_length=300)),
                ('username', models.CharField(max_length=30, validators=[django.core.validators.RegexValidator(re.compile('^[\\w.+-]+$', 32), 'Username can only contain letters, digits or the following characters: ./+/-/_', 'invalid')], verbose_name='Username', unique=True)),
                ('email', models.EmailField(max_length=150, unique=True, verbose_name='Email')),
                ('bio', models.TextField(blank=True, null=True, verbose_name='Bio')),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=6, default=('Male', 'Male'))),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Birth Date')),
                ('profile_image', models.CharField(max_length=500, default='/static/4ideas/img/default.png')),
                ('cover_image', models.CharField(max_length=500, default='/static/4ideas/img/cover.jpeg')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active?')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Is admin?')),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups', related_query_name='user', related_name='user_set', to='auth.Group')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions', related_query_name='user', related_name='user_set', to='auth.Permission')),
            ],
            options={
                'verbose_name_plural': 'Players',
                'verbose_name': 'Player',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
