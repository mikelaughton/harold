# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IPR_calculators', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='calculator',
            name='title',
            field=models.CharField(default='BWAH', max_length='255'),
            preserve_default=False,
        ),
    ]
