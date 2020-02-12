from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


def top(request):
    # template = loader.get_template('base_app/top.html')
    ctx = {'title': 'Django学習ちゃんねる(仮)'}
    return render(request, 'base_app/top.html', ctx)
    # return HttpResponse(template.render(ctx, request))
