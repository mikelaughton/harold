# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IPR_calculators_cms_integration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssociatedItems',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('plugin', models.ForeignKey(related_name='associated_items', to='IPR_calculators_cms_integration.CalculatorPluginModel')),
            ],
        ),
    ]
