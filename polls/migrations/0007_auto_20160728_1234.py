# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20160728_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_type',
            field=models.CharField(choices=[('CH', 'Multiple choice'), ('TE', 'Text'), ('CO', 'Country'), ('WS', 'Word scale'), ('NS', 'Number scale'), ('TF', 'True or false')], max_length=2),
        ),
    ]
