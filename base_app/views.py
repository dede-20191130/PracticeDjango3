from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from django.views.generic import TemplateView


class TopView(TemplateView):
    template_name = 'base_app/top.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['title'] = 'IT学習ちゃんねる(仮)'
        return ctx
