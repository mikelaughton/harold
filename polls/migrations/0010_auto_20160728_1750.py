# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_question_evaluator'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='evaluator',
        ),
        migrations.AddField(
            model_name='survey',
            name='evaluator',
            field=models.CharField(max_length=200, blank=True),
        ),
    ]
