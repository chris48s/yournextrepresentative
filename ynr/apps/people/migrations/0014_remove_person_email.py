# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-12 09:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("people", "0013_populate_favourite_biscuit")]

    operations = [migrations.RemoveField(model_name="person", name="email")]