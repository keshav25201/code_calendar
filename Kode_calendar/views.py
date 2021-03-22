from django.http.response import Http404, HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    context = {}
    return render(request, "Kode_calendar/home.html", context)


def all(request):
    context = {}
    return render(request, "Kode_calendar/all.html", context)
