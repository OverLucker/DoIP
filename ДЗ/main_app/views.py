from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse
from django.template import loader

from .models import Participant, Event, Participation



# def index(request):
    # return HttpResponse("<h1>Hello, world!</h1>")
    
def events_page(request):
    template = loader.get_template('main_app/index.html')
    context = { 
        'items' : renderUtil(request, 0),
    }
    return HttpResponse(template.render(context, request))
      
    
def events_page_part(request, page_id):
    html = renderUtil(request, page_id)
    return HttpResponse(html)
    
def event_page(request, id):
    try:
        pid = int(id)
        event = get_object_or_404(Event, id=pid)
        template = loader.get_template('main_app/event.html')
        page_id = int(event.id / 10)
        context = {
            'event': event, 
            'is_part': False,
            'page_id' : page_id,
        }
        return HttpResponse(template.render(context, request))
    except ValueError:
        return HttpResponse(template.render(context, request))
   
def renderUtil(request, page_id):
    pid = int(page_id)
    events = Event.objects.all()[pid * 10: (pid+1) * 10]
    template = loader.get_template('main_app/page.html')
    context = {
        'events': events, 
    }
    return template.render(context, request)