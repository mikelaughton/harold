from django.db import models
from cms.models import CMSPlugin
from polls.models import Survey
# Create your models here.

#Because DjangoCMS
class SurveyPluginModel(CMSPlugin):
	survey = models.ForeignKey(Survey)
	def __str__(self):
		return self.survey.title