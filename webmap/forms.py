#this is the python code that will get the user input from the html page(from javascript script). Then it will store into the database

from django import forms 
from .models import datepicker, Userlocation
  
# creating a form  
class dateForm(forms.ModelForm): 
    class Meta:
        model = datepicker
        fields = ['startdate', 'enddate']

class locationForm(forms.ModelForm):
    class Meta:
        model = Userlocation
        fields = ['user_latitude', 'user_longitude']