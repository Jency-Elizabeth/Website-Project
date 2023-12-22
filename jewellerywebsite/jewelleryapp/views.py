from django.http import HttpResponse
from django.shortcuts import render
from .models import Jewellery


# Create your views here.
def index(request):
    obj = Jewellery.objects.all()
    return render(request, 'index.html',{'jewells':obj})
