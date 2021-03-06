#-*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import generic

from .models import Choice, Question, Survey, Response
from .forms import *

import json

def booya(request,response_id):
	#Delete almost immediately.
	context = {'response':get_object_or_404(Response,pk=response_id)}
	return render(request,'polls/booya.html',context)

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_poll_list'

    def get_queryset(self):
        return Survey.objects.all()[:5]


class DetailView(generic.DetailView):
    model = Survey
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def respond(request,survey_id):
    #You goofed this, you need to create a JSON array such that you have { "response":{ "question_pk":question_pk, "answer": answer },{ "question_pk":question_pk, "answer":answer } ... }
	survey = get_object_or_404(Survey,pk=survey_id)
	if request.method == 'POST':
		form = ResponseForm(survey,request.POST)
		if form.is_valid():
		    #Create list of dictionaries
			r_raw = [ {'question':qpk, 'answer':answer } for qpk,answer in list( form.cleaned_data.items() ) ]
			r_text = json.dumps(r_raw)
			response = Response(survey=survey,response_text=r_text)
			response.save()
			return HttpResponseRedirect(reverse('polls:booya',kwargs={'response_id':response.pk}))
	else:
		form = ResponseForm(survey)
	context = { 'survey':survey, 'form':form }
	#Pass on this lad, look it up.
	return render(request,'polls/respond.html',context)

class Respond(generic.CreateView):
    model = Survey
    form_class = ResponseForm
    success_url = 'success/' #replace with url.reverse
    template_name = 'polls/create.html'

    def get(self,request,*args,**kwargs):
        # Does GET requests, returns blank formsets.
        self.object = None
        #Returns SurveyForm
        form_class = self.get_form_class()
        #Creates original form?
        form = self.get_form(form_class)
        return self.render_to_response(self.get_context_data(form=form))

    def post(self,request,*args,**kwargs):
        pass

    def form_valid(self,form,poll_form):
        pass

    def form_invalid(self,form,poll_form):
        pass

def vote(request, poll_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render(request, 'polls/detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
