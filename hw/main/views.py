from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist

from django.views import View

from django.http import HttpResponse

# local imports
from .models import Event
from .forms import AuthForm, RegistrationForm, AddEventForm

from django.core.files import File
from django.core.files.storage import FileSystemStorage


from django.contrib.staticfiles.templatetags.staticfiles import static
import os


# Create your views here.

    
# Base for all View instances in my code, 
#   modifies context to render base.html properly
class BaseView(View):
    def get(self, request, template ,context):
        context.update ({
            'authorized' : request.user.is_authenticated,
            'user' : { 'name' : request.user.username },
        })
        
        return render(request, template, context)
    
    
# View displaying 2 forms : AuthForm & RegistrationForm
class LogRegView(BaseView):
    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
       
        authForm = AuthForm()
        regForm = RegistrationForm()
        
        return super().get(request, 'registration/login.html', {
                'registration_form': regForm,
                'login_form' : authForm,
            })

            
# register new user & login it
def register(request):
    # form = RegistrationForm(request.POST)
    username = request.POST.get("username")
    password1 = request.POST.get("password1")
    password2 = request.POST.get("password2")
    if (password1 == password2):
        
        if (User.objects.filter(username = username).exists()):
            resp = {"error" : "Already busy"}
            return HttpResponse(resp)
            
        # register now    
        user = User.objects.create_user(username = username, password = password1)
        request.POST = request.POST.copy()
        request.POST["password"]=password1
        return auth(request)

    return HttpResponse("Error")
  

# login users  
def auth(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = authenticate(username = username, password = password)
    if user is not None:
        login(request, user)
        return redirect('main_page')
    return redirect('login_url')

    
# returns requested page
def page_request(request, page_id):
    context = {
        'events' : ObjectListView.get_page_dict(page_id),
    }
    return render_to_response('main/base_list.html', context)
    
    
    
# Main Page view, lists all objects
class ObjectListView(BaseView): 
    objOnList = 10
    
    
    def get_page_dict(page_id):
        page_id = int(page_id)
        end = len(Event.objects.all()) - ObjectListView.objOnList * page_id
        if end < 0:
            end = 0
            start = 0
        else:
            start = end - ObjectListView.objOnList
            if start < 0 :
                start = 0
        
        #need to cut description
        all = Event.objects.all()[start: end][::-1]
        
        for i in all:
            if len(i.desc) > 200:
                i.desc = i.desc[:200] + '...'
        return all
        
        
    def get(self, request):
        context = {
            'name' : 'Events',
            'events': ObjectListView.get_page_dict(0),
            'add_form' : AddEventForm(),
        }
        return super().get(request, 'main/main.html', context)


# View 
class ObjectView(BaseView):
    def get(self, request, event_id):
        try:
            obj = get_object_or_404(Event, id = event_id)
            obj.participation.get(id=request.user.id)
            status = True
        except ObjectDoesNotExist:
            status = False

        context = {
            'event' : obj,
            'status' : status
        }
        return super().get(request, 'object/object.html', context)
        
    # @login_required(redirect_field_name='login_url')
    def post(self, request, event_id):
        # ToDo : check if correct
        # try:
        event = Event.objects.get(id=event_id)
        if request.user.is_authenticated():
            state = request.POST.get('state')
            
            
            if state == 'True' and not event.participation.filter(id=request.user.id).exists():
                try:
                    event.participation.add(request.user)
                except Exception:
                    return HttpResponse("Add 2 " + str(request.user.id))

            
            if state == 'False' and event.participation.filter(id=request.user.id).exists():
                try:
                    event.participation.remove(User.objects.get(id=request.user.id))
                except Exception:
                    return HttpResponse("Delete 2")

        
        context = { 'users' : event.participation.all() }
        return render_to_response('object/base_user_list.html', context)
        

        
def add_obj(request):
    form = AddEventForm(request.POST)
    
    if form.is_valid():
        event = form.fill_object()
        
        #saving file
        f = File(request.FILES["image"])
        fs = FileSystemStorage()
        file_url = r'images/pokemons/%d%s' % (event.id, '.jpg')
        uploaded_file_url = 'main/static/main/'+file_url
        filename = fs.save(uploaded_file_url, f)
        
        event.imageUrl = file_url
        event.save()
        return redirect('main_page')
    return HttpResponse(form.errors)
    