# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0012_auto_20160804_0005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_type',
            field=models.CharField(max_length=2, choices=[('CH', 'Multiple choice'), ('TE', 'Text'), ('LT', 'Long text'), ('CO', 'Country'), ('WS', 'Word scale'), ('NS', 'Number scale'), ('TF', 'True or false')]),
        ),
    ]
