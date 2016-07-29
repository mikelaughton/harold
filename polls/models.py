#-*- coding: utf-8 -*-
from django.db import models
from django.core.exceptions import ValidationError
import re
from polls import eqparser
#from django.utils.translation import ugettext_lazy as _
#I18n later.
def _(text):
    return text

class Survey(models.Model):
    title = models.CharField(max_length=200)
    evaluator = models.CharField(max_length=200,blank=True)
    def __str__(self):
        return self.title

class Response(models.Model):
    #Build this into a pseudo-JSON thing.
    survey = models.ForeignKey(Survey)
    #This means you have to write a separate view to edit the response.
    response_text = models.TextField()
    def get_response_to_question(self,question):
        pass

    def parse_equation(self):
        #Really bad parser.
        questions_identified = re.findall("({\d+})",self.survey.eq)
        for question in questions_identified:
            self.get_response_to_question(question)

#This may need subclassing.
class Question(models.Model):
    qtypes = (('CH',_('Multiple choice')),
              ('TE',_('Text')),
              ('CO',_('Country')),
              ('WS',_('Word scale')),
              ('NS',_('Number scale')),
              ('TF',_('True or false')),
                )
    survey = models.ForeignKey(Survey,blank=True,null=True)
    question = models.CharField(max_length=200)
    question_type = models.CharField(max_length=2,choices=qtypes)
    weight = models.DecimalField(max_digits=3,decimal_places=3)
    
    def primary_key(self):
        return self.pk

    primary_key = property(primary_key)

    @property
    def choices(self):
        return self.choice_set.all()
    @property
    def choice_tuple(self):
        return ((c.choice_value,c.choice_text) for c in self.choices)
    @property
    def choices_values(self):
        return (c.choice_value for c in self.choices)

    @property
    def choices_text(self):
        return (c.choice_text for c in self.choices)

    def clean(self):
        #Ripe for testing m'lad
        if self.question_type == "TF":
            if len(self.choices)>2:
                raise ValidationError(_("True/false questions must have only two options, True and False."))
            if not all([a=="True" or "False" for a in self.choices_values]):
                raise ValidationError(_("True/false questions must have only two options, True and False."))

    def __str__(self):  # Python 3: def __str__(self):
        return self.question

class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    choice_value = models.CharField(max_length=20,blank=True)
    def __str__(self):  # Python 3: def __str__(self):
        return self.choice_text
