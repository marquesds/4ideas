# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
import re
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(verbose_name='last login', null=True, blank=True)),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('name', models.CharField(max_length=300)),
                ('username', models.CharField(validators=[django.core.validators.RegexValidator(re.compile('^[\\w.+-]+$', 32), 'Username can only contain letters, digits or the following characters: ./+/-/_', 'invalid')], max_length=30, verbose_name='Username', unique=True)),
                ('email', models.EmailField(max_length=150, verbose_name='Email', unique=True)),
                ('bio', models.TextField(verbose_name='Bio', null=True, blank=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default=('Male', 'Male'), max_length=6)),
                ('birth_date', models.DateField(verbose_name='Birth Date', null=True, blank=True)),
                ('profile_image', models.CharField(default='/static/4ideas/img/female.png', max_length=500)),
                ('cover_image', models.CharField(default='/static/4ideas/img/cover.jpeg', max_length=500)),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active?')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Is admin?')),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('groups', models.ManyToManyField(to='auth.Group', verbose_name='groups', blank=True, related_query_name='user', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set')),
                ('user_permissions', models.ManyToManyField(to='auth.Permission', verbose_name='user permissions', blank=True, related_query_name='user', help_text='Specific permissions for this user.', related_name='user_set')),
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
