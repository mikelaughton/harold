from django import forms
from .models import *

class SurveyForm(forms.ModelForm):
    class Meta:
    	model = Survey
    	fields = ['title']
    	
class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ['question']

class ChoicesForm(forms.ModelForm):
    class Meta:
        model=Choice
        fields=['choice_text']
