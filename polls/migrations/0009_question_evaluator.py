# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_choice_choice_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='evaluator',
            field=models.CharField(max_length=200, blank=True),
        ),
    ]
