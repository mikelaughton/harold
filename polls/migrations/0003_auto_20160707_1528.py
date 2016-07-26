# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_disclaimer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='disclaimer',
            name='poll',
        ),
        migrations.DeleteModel(
            name='Disclaimer',
        ),
        migrations.AddField(
            model_name='poll',
            name='survey',
            field=models.ForeignKey(null=True, to='polls.Survey', blank=True),
        ),
    ]
