# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-22 11:39
from __future__ import unicode_literals

from django.db import migrations


def populate_initial_candidate_counts(apps, schema_editor):
    Party = apps.get_model("parties", "Party")
    parties_qs = Party.objects.all()
    for party in parties_qs:
        party.total_candidates = party.membership_set.count()
        party.current_candidates = party.membership_set.filter(
            post_election__election__current=True
        ).count()
        party.save()


class Migration(migrations.Migration):

    dependencies = [("parties", "0010_add_candidate_totals")]

    operations = [
        migrations.RunPython(
            populate_initial_candidate_counts, migrations.RunPython.noop
        )
    ]