from django.shortcuts import render
from .models import Route, RouteTypes, RoutePoint


def main(request):
    buses = Route.objects.filter(type=RouteTypes.BUS)
    trolleybuses = Route.objects.filter(type=RouteTypes.TROLLEYBUS)

    return render(request, 'index.html', {'buses': buses, 'trolleybuses': trolleybuses})


def schedule(request):
    routes = RoutePoint.objects.filter(route=Route)

    return render(request, 'schedule.html', {'routes': routes})


def bus_schedule(request):
    return render(request, 'bus_schedule.html', {})