from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from polls_cms_integration.models import SurveyPluginModel
from django.utils.translation import ugettext as _
from polls.forms import ResponseForm

class SurveyPluginPublisher(CMSPluginBase):
	model = SurveyPluginModel
	module = _("Surveys")
	name = _("Survey plugin")
	render_template = "polls_cms_integration/poll_plugin.html"

	def render(self,context,instance,placeholder):
		form = ResponseForm(instance.survey)
		context.update({'instance':instance,'form':form})
		return context
		
plugin_pool.register_plugin(SurveyPluginPublisher)