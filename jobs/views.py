from django.shortcuts import render
from .models import Job #this is used to fetch the data from database

# Create your views here.
def home(request):
    jobs=Job.objects   #  this is used to fetch the data from databases
    return render(request,'jobs/home.html',{'jobs':jobs})