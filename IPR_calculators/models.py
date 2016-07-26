from django.db import models

# Create your models here.

class Question(models.Model):
	QTYPES = (
		('BOOL','Binary'),
		('INTE','Expects integer'),
		('MULT','Multiple choice'),
		('TEXT','Normal text'),
	)
	survey = models.ForeignKey(Survey)
	coefficient = models.IntegerField(default=1)	
	question_text = models.CharField(max_length=255)
	exponent = models.IntegerField(default=1)
	type = models.CharField(max_length=10,choices=self.QTYPES)
	def __str__(self):
		return self.question_text

def QuestionResponse(models.Model):
	question = models.ForeignKey(Question)
	answer = models.

class Calculator(models.Model):
	title = models.CharField(max_length="255")
	questions = models.ManyToManyField(Question)
	def __str__(self):
		return self.question_text

class Evaluator(models.Model):
	pass

class Response(models.Model):
	email = models.EmailField()
	date = models.DateField(auto_now=True)
	calculator = models.ForeignKey(Calculator)
	evaluator = models.ForeignKey(Evaluator)
