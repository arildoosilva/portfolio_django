#from django.http import HttpResponse
from django.shortcuts import render_to_response
from .models import Line
from .models import Background


def home(request):
    #return HttpResponse('Hello world.')
    #return render_to_response('portfolio/base.html', {'texto': Line.objects.all()})
    return render_to_response('portfolio/index.html', {'texto': Line.objects.all(), 'background': Background.objects.all()})
