# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_auto_20160728_1234'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='choice_value',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
