from django.http import response
from django.http.response import Http404, HttpResponse
from django.shortcuts import render
import requests, json
from datetime import date, datetime, timedelta

# Create your views here.
def days(strt_time):
    one_day_ahead = str(timedelta(days=1) + datetime.now())
    c1, c2, c3 = int(strt_time[:4]), int(strt_time[5:7]), int(strt_time[8:10])
    a1, a2, a3 = (
        int(one_day_ahead[:4]),
        int(one_day_ahead[5:7]),
        int(one_day_ahead[8:10]),
    )
    diff = str(datetime(a1, a2, a3) - datetime(c1, c2, c3))
    if diff == 0:
        return 1
    elif diff == 1:
        return 0
    else:
        return -1


def make_api_calls():
    response = requests.get("https://www.kontests.net/api/v1/all")
    python_data = json.loads(response.text)
    today, tomorrow = list(), list()
    for contests in python_data:
        getime = days(contests["start_time"])
        # print(contests["name"], getime)
        if getime == 0:
            today.append(contests)
        elif getime == 1:
            tomorrow.append(contests)
    # print(today)
    # print(tomorrow)
    return today, tomorrow


def home(request):
    today, tomorrow = make_api_calls()
    # if not (today) and not (tomorrow):
    # return render(request, "Kode_calendar/all.html")
    context = {"today": today, "tomorrow": tomorrow}
    return render(request, "Kode_calendar/home.html", context)


def all(request):
    context = {}
    return render(request, "Kode_calendar/all.html", context)
