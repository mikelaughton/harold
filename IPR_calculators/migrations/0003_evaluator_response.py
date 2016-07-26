# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IPR_calculators', '0002_calculator_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evaluator',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('email', models.EmailField(max_length=254)),
                ('date', models.DateField(auto_now=True)),
                ('calculator', models.ForeignKey(to='IPR_calculators.Calculator')),
                ('evaluator', models.ForeignKey(to='IPR_calculators.Evaluator')),
            ],
        ),
    ]
