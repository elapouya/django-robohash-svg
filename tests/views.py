#
# Created : 2018-03-22
#
# @author: Eric Lapouyade
#

from django.views.generic import TemplateView
from random import random

class IndexView(TemplateView):
    template_name = 'tests/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['random'] = str(random())
        return context
