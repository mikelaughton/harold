#-*- coding: utf-8 -*-
from django.db import models

#I18n later.
def _(text):
    return text

class Survey(models.Model):
    title = models.CharField(max_length=200)
    def __str__(self):
        return self.title

class Poll(models.Model):
    qtypes = (('CH',_('Multiple choice')),
              ('TE',_('Text')),
              ('CO',_('Country')),
              ('WS',_('Word scale')),
              ('NS',_('Number scale')),
                )
    survey = models.ForeignKey(Survey,blank=True,null=True)
    question = models.CharField(max_length=200)
    question_type = models.CharField(max_length=2,choices=qtypes)
    weight = models.DecimalField(max_digits=3,decimal_places=3)

    @property
    def choices(self):
        return self.choice_set.all()

    def __str__(self):  # Python 3: def __str__(self):
        return self.question


class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):  # Python 3: def __str__(self):
        return self.choice_text
