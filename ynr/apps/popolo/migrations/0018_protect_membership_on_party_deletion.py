# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-09-13 14:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("popolo", "0017_remove_membership_on_behalf_of")]

    operations = [
        migrations.AlterField(
            model_name="membership",
            name="party",
            field=models.ForeignKey(
                help_text="The political party for this membership",
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="parties.Party",
            ),
        )
    ]