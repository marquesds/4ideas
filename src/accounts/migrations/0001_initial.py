# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.auth.models
import django.core.validators
import re


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(null=True, blank=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(help_text='Designates that this user has all permissions without explicitly assigning them.', default=False, verbose_name='superuser status')),
                ('name', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=30, unique=True, verbose_name='Username', validators=[django.core.validators.RegexValidator(re.compile('^[\\w.+-]+$', 32), 'Username can only contain letters, digits or the following characters: ./+/-/_', 'invalid')])),
                ('email', models.EmailField(unique=True, verbose_name='Email', max_length=150)),
                ('bio', models.TextField(null=True, blank=True, verbose_name='Bio', max_length=5000)),
                ('gender', models.CharField(max_length=6, default=('Male', 'Male'), choices=[('Male', 'Male'), ('Female', 'Female')])),
                ('birth_date', models.DateField(null=True, blank=True, verbose_name='Birth Date')),
                ('profile_image', models.CharField(default='/static/4ideas/img/default.png', max_length=300)),
                ('cover_image', models.CharField(default='/static/4ideas/img/cover.jpeg', max_length=300)),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active?')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Is admin?')),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('groups', models.ManyToManyField(related_query_name='user', blank=True, verbose_name='groups', related_name='user_set', to='auth.Group', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.')),
                ('user_permissions', models.ManyToManyField(related_query_name='user', blank=True, verbose_name='user permissions', related_name='user_set', to='auth.Permission', help_text='Specific permissions for this user.')),
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
