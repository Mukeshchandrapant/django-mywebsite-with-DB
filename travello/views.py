from django.shortcuts import render
from .models import Destination

# Create your views here.


def index(request):

    dest_list = Destination.objects.all()

    return render(request, "index.html", {'dest_list': dest_list})

