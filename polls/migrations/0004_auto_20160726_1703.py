# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20160707_1528'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='question_type',
            field=models.CharField(choices=[('CH', 'Multiple choice'), ('TE', 'Text'), ('CO', 'Country'), ('WS', 'Word scale'), ('NS', 'Number scale')], default='CH', max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='poll',
            name='weight',
            field=models.DecimalField(default=0.0, max_digits=3, decimal_places=3),
            preserve_default=False,
        ),
    ]
