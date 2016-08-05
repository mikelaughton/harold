# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0012_auto_20160804_0005'),
        ('cms', '0014_auto_20160404_1908'),
    ]

    operations = [
        migrations.CreateModel(
            name='SurveyPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(serialize=False, auto_created=True, to='cms.CMSPlugin', parent_link=True, primary_key=True)),
                ('survey', models.ForeignKey(to='polls.Survey')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
