#-*- coding: utf-8 -*-
from django.contrib import admin

from .models import Choice, Poll, Survey
import nested_admin

class ChoiceInline(nested_admin.NestedTabularInline):
    model = Choice
    readonly_fields = ('votes',)
    extra = 3

class PollInline(nested_admin.NestedTabularInline):
    model = Poll
    fieldsets = [
        (None, {
            'fields': ('question','question_type'),
        }),
    ]
    inlines = [ChoiceInline]
    list_display = ('question',)
    search_fields = ['question']

class SurveyAdmin(nested_admin.NestedModelAdmin):
    model = Survey
    inlines = [PollInline]


admin.site.register(Survey,SurveyAdmin)

