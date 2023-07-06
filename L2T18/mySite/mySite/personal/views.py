from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):

    return render(request, "index.html", {'name': 'Joshua'})

def previously_created_1(request):

    return render(request, "previously created 1.html")
