from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def simple_request (request) :
    return render ( request, 'main/index.html' )
    
def orders_request (request) :
    #return HttpResponse("hello world!")
    context = {
        'orders' : [
            {
                'id' : 1,
                'title' : 'Первый заказ',
            },
            {
                'id' : 2,
                'title' : 'Второй заказ',
            },
            {
                'id' : 3,
                'title' : 'Третий заказ',
            },
        ]
    }
    return render ( request, 'main/orders.html', context )
    
def order_request( request, id ) :
    return HttpResponse( "hello world!" )