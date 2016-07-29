#-*- coding: utf-8 -*-
from django.contrib import admin

from .models import Choice, Question, Survey
import nested_admin



class ChoiceInline(nested_admin.NestedTabularInline):
    model = Choice
    extra = 2

class QuestionInline(nested_admin.NestedTabularInline):
    model = Question
    fieldsets = [
        (None, {
            'fields': ('question','question_type','weight',),
        }),
        (None, {
            'fields': ('primary_key',),
        }),
    ]
    inlines = [ChoiceInline]
    list_display = ('question','primary_key')
    readonly_fields = ('primary_key',)
    search_fields = ['question']

class SurveyAdmin(nested_admin.NestedModelAdmin):
    model = Survey
    inlines = [QuestionInline]
    save_as = True
    actions_on_top = True


admin.site.register(Survey,SurveyAdmin)
admin.site.register(Question)

