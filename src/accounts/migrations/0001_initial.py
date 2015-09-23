# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import re
import django.core.validators
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(verbose_name='last login', blank=True, null=True)),
                ('is_superuser', models.BooleanField(default=False, verbose_name='superuser status', help_text='Designates that this user has all permissions without explicitly assigning them.')),
                ('name', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=30, verbose_name='Username', unique=True, validators=[django.core.validators.RegexValidator(re.compile('^[\\w.+-]+$', 32), 'Username can only contain letters, digits or the following characters: ./+/-/_', 'invalid')])),
                ('email', models.EmailField(max_length=150, verbose_name='Email', unique=True)),
                ('bio', models.TextField(max_length=5000, verbose_name='Bio', blank=True, null=True)),
                ('gender', models.CharField(null=True, max_length=6, blank=True, choices=[('Male', 'Male'), ('Female', 'Female')])),
                ('birth_date', models.DateField(verbose_name='Birth Date', blank=True, null=True)),
                ('profile_image', models.CharField(max_length=300, default='/static/4ideas/img/default.png')),
                ('cover_image', models.CharField(max_length=300, default='/static/4ideas/img/cover.jpeg')),
                ('is_active', models.BooleanField(verbose_name='Is active?', default=True)),
                ('is_staff', models.BooleanField(verbose_name='Is admin?', default=False)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('groups', models.ManyToManyField(related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups', related_query_name='user')),
                ('user_permissions', models.ManyToManyField(related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions', related_query_name='user')),
            ],
            options={
                'verbose_name': 'Player',
                'verbose_name_plural': 'Players',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
