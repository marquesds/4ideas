# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import re
import django.contrib.auth.models
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
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(default=False, verbose_name='superuser status', help_text='Designates that this user has all permissions without explicitly assigning them.')),
                ('name', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=30, unique=True, verbose_name='Username', validators=[django.core.validators.RegexValidator(re.compile('^[\\w.+-]+$', 32), 'Username can only contain letters, digits or the following characters: ./+/-/_', 'invalid')])),
                ('email', models.EmailField(max_length=150, verbose_name='Email', unique=True)),
                ('bio', models.TextField(null=True, verbose_name='Bio', blank=True)),
                ('gender', models.CharField(default=('Male', 'Male'), choices=[('Male', 'Male'), ('Female', 'Female')], max_length=6)),
                ('birth_date', models.DateField(null=True, verbose_name='Birth Date', blank=True)),
                ('profile_image', models.CharField(default='/static/4ideas/img/default.png', max_length=300)),
                ('cover_image', models.CharField(default='/static/4ideas/img/cover.jpeg', max_length=300)),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active?')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Is admin?')),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('groups', models.ManyToManyField(to='auth.Group', related_name='user_set', blank=True, related_query_name='user', verbose_name='groups', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.')),
                ('user_permissions', models.ManyToManyField(to='auth.Permission', related_name='user_set', blank=True, related_query_name='user', verbose_name='user permissions', help_text='Specific permissions for this user.')),
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
