from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from django.views.generic import TemplateView, ListView

from thread_app.models import Topic


def top(request):
    # template = loader.get_template('base/top.html')
    ctx = {'title': 'IT学習ちゃんねる(仮)'}
    # return HttpResponse(template.render(ctx, request))
    return render(request, 'base_app/top.html', ctx)


class TopView(TemplateView):
    template_name = 'base_app/top.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['title'] = 'IT学習ちゃんねる(仮)'
        return ctx


class TopicListView(ListView):
    template_name = 'base_app/top.html'
    model = Topic
    queryset = Topic.objects.order_by('-created')
    context_object_name = 'topic_list'
