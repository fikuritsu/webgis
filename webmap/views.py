#this the python code that controls what is happening in a page. the urls.py get the page attributes from here

from django.shortcuts import render, redirect
from django.core.serializers import serialize
from django.http import HttpResponse
from  django.views import generic
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from .models import PointsOrder, Att456, Riverdata, datepicker, Shop, Userlocation, Hotpoints
from .forms import dateForm, locationForm 
from django.contrib import messages
import datetime

# Create your views here.

def river(request):
    riverData= serialize('geojson', Riverdata.objects.all())
    return HttpResponse(riverData, content_type='geojson')

def marker(request):
    # fromdate = datepicker.object
    # datepicker.objects.values('startdate')..order_by('-id').filter(pk=1)[0]['startdate']
    fromdate= datepicker.objects.values('startdate').order_by('-id')[0]['startdate']
    todate= datepicker.objects.values('enddate').order_by('-id')[0]['enddate']
    # return HttpResponse(markerData, content_type='json')
    markerData= serialize('geojson', Hotpoints.objects.filter(date__range=[fromdate,todate]))
    return HttpResponse(markerData, content_type='geojson')



def testing(request):
    if request.method == 'POST':
        form = dateForm(request.POST or None)

        if form.is_valid():
            form.save()
            fromdate= datepicker.objects.values('startdate').order_by('-id')[0]['startdate']
            startdate = fromdate.strftime("%b %d, %Y")
            todate= datepicker.objects.values('enddate').order_by('-id')[0]['enddate']
            enddate = todate.strftime("%b %d, %Y")
            messages.success(request, (" The data shown below is from "+ startdate + " until " +  enddate))


            return redirect('testing')
    
    else:


        return render(request, 'test.html')

def index(request):
    return render(request, 'index.html')

# def home(request):
#     return render(request, 'home.html')

# def testing(request):
#     return render(request, 'test.html')

class Home(generic.ListView):
    template_name = "calculate.html"
    context_object_name = "shops"

    def get_queryset(self):
        model = Shop
        latitude = Userlocation.objects.values('user_latitude').order_by('-id')[0]['user_latitude']
        longitude = Userlocation.objects.values('user_longitude').order_by('-id')[0]['user_longitude']
        user_location = Point(longitude, latitude, srid=4326)
        return Shop.objects.annotate(distance=Distance("location", user_location)).order_by("distance")[0:6]

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        # latitude = Userlocation.objects.values('user_latitude').order_by('-id')[0]['user_latitude']
        # longitude = Userlocation.objects.values('user_longitude').order_by('-id')[0]['user_longitude']
        context['userlatitude'] = Userlocation.objects.values('user_latitude').order_by('-id')[0]['user_latitude']
        context['userlongitude'] = Userlocation.objects.values('user_longitude').order_by('-id')[0]['user_longitude']
        return context


def radius(request):
    if request.method == 'POST':
        form = locationForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, ("Query successful"))
            return redirect('loading')

    else:
        return render(request, 'radius.html')

def loading(request):
    return render(request, 'load.html')
