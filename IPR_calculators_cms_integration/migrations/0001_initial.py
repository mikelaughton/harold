# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0014_auto_20160404_1908'),
        ('IPR_calculators', '0003_evaluator_response'),
    ]

    operations = [
        migrations.CreateModel(
            name='CalculatorPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(to='cms.CMSPlugin', parent_link=True, serialize=False, auto_created=True, primary_key=True)),
                ('calculator', models.ForeignKey(to='IPR_calculators.Calculator')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
