import csv

from django.shortcuts import render
from django.http import HttpResponse

from . import models

# Create your views here.
def index(request):
    return HttpResponse('OK')


def upload_flights(request):
    with open('flights.csv', 'r') as f:
        reader = csv.reader(f)
        for ori, des, dur in reader:
            flights = models.Flights(origin=ori, destination=des, duration=dur)
            flights.save()
    return HttpResponse('Upload completed')


def upload_passengers(request):
    with open('passengers.csv', 'r') as p:
        reader = csv.reader(p)
        for name, flight_id in reader:
            flight = models.Flights.objects.get(id=flight_id)
            passengers = models.Passengers(name=name, flight_id=flight)
            passengers.save()
    return HttpResponse('Upload completed')