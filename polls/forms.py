from django import forms
from polls.models import Survey, Question, Choice
#For the renderer
from django.utils.safestring import mark_safe

#Shamelessly grabbed from HighLife, http://stackoverflow.com/questions/5935546/align-radio-buttons-horizontally-in-django-forms
class HorizontalRadioRenderer(forms.RadioSelect.renderer):
  def render(self):
    return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))

class ResponseForm(forms.Form):
    
    def __init__(self,survey,*args,**kwargs):
        super(ResponseForm,self).__init__(*args,**kwargs)
        #Expects survey
        self.survey = survey
        for question in self.survey.question_set.all():
            qchoices = question.choice_tuple
            if question.question_type == "CH":
                self.fields['qpk{}'.format(question.pk)]=forms.ChoiceField(label=question.question,choices=qchoices,widget=forms.RadioSelect(renderer=HorizontalRadioRenderer))
            if question.question_type == "TE":
                self.fields['qpk{}'.format(question.pk)] = forms.CharField()
            if question.question_type == "TF":
                self.fields['qpk{}'.format(question.pk)] = forms.ChoiceField(label=question.question, choices=qchoices, widget = forms.RadioSelect(renderer=HorizontalRadioRenderer))
            if question.question_type == "LT":
                self.fields['qpk{}'.format(question.pk)] = forms.CharField(label=question.question,widget=forms.Textarea)
