from django.shortcuts import render, get_object_or_404
from .models import Event


def object_list(request, page_id):
    objects_on_list = 10
    page_id = int(page_id if page_id else 0)
    end = len(Event.objects.all())
    tmp = end - objects_on_list * page_id
    end = tmp if tmp > 0 else 0
    tmp = end - objects_on_list
    start = tmp if tmp > 0 else 0
    lst = Event.objects.all()[start:end:-1]
    return render(
        request,
        'index.html',
        context={
            'page': {'title': 'List'},
            'list': lst,
        }
    )


def object(request, object_id):
    return render(
        request,
        'single_object.html',
        context={
            'object': get_object_or_404(Event, id=object_id),
        }
    )
