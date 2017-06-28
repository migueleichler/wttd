# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-20 03:44
from __future__ import unicode_literals

from django.db import migrations, models

import eventex.subscriptions.validators


class Migration(migrations.Migration):
    dependencies = [
        ('subscriptions', '0002_auto_20170610_0250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='cpf',
            field=models.CharField(max_length=11, validators=[
                eventex.subscriptions.validators.validate_digits_only,
                eventex.subscriptions.validators.validate_has_11_chars],
                                   verbose_name='CPF'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='email',
            field=models.EmailField(blank=True, max_length=254,
                                    verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='phone',
            field=models.CharField(blank=True, max_length=20,
                                   verbose_name='telefone'),
        ),
    ]