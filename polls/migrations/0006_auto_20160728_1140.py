# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_remove_choice_votes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('question', models.CharField(max_length=200)),
                ('question_type', models.CharField(max_length=2, choices=[('CH', 'Multiple choice'), ('TE', 'Text'), ('CO', 'Country'), ('WS', 'Word scale'), ('NS', 'Number scale')])),
                ('weight', models.DecimalField(decimal_places=3, max_digits=3)),
                ('survey', models.ForeignKey(to='polls.Survey', null=True, blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='poll',
            name='survey',
        ),
        migrations.RemoveField(
            model_name='choice',
            name='poll',
        ),
        migrations.DeleteModel(
            name='Poll',
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(to='polls.Question', default=1),
            preserve_default=False,
        ),
    ]
