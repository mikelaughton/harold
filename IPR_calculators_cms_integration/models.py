from django.db import models
from cms.models import CMSPlugin
from IPR_calculators.models import *
# Create your models here.

class CalculatorPluginModel(CMSPlugin):
	calculator = models.ForeignKey(Calculator)
	def __str__(self):
		return self.calculator.title

class AssociatedItems(models.Model):
	plugin = models.ForeignKey(CalculatorPluginModel,related_name="associated_items")
	def copy_relations(self,old_instance):
		self.questions = old_instance.questions.all()
