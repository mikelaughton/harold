# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0011_response'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='weight',
        ),
        migrations.AlterField(
            model_name='survey',
            name='evaluator',
            field=models.CharField(help_text='Leave this blank for the first save. Enter values such as .5{1}+.5{2} for two equally weighted questions.', blank=True, max_length=200),
        ),
    ]
