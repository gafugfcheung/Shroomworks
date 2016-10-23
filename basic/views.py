from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from .models import Pic
from django.contrib import messages
from django.core.urlresolvers import reverse
import datetime
from .forms import PicForm


def index(request):
    pic_list = Pic.objects.order_by('-pub_date')
    template = loader.get_template('basic/index.html')

    if request.method == 'POST':
        form = PicForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = PicForm()
    context = {'pic_list': pic_list, 'form': form}
    return HttpResponse(template.render(context, request))

def detail(request, pic_id):
    response = "You're looking at the results of pic %s."
    return HttpResponse(response % pic_id)

def add(request, x):
    pic = PicForm(request.POST)
    pic.save()
    lat1 = request.POST['lat']
    lng1 = request.POST['lng']
    return HttpResponseRedirect('/basic/')
