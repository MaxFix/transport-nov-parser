from django.shortcuts import render
from .models import Route, RouteTypes, RoutePoint


def main(request):
    buses = Route.objects.filter(type=RouteTypes.BUS)
    trolleybuses = Route.objects.filter(type=RouteTypes.TROLLEYBUS)

    return render(request, 'index.html', {'buses': buses, 'trolleybuses': trolleybuses})

def schedule(request):
    route = Route.objects.filter(code=request.GET['mar']).first()
    stops = RoutePoint.object.filter(route=route)

    return render(request, 'schedule.html', {'stops': stops})

def bus_schedule(request):
    return render(request, 'bus_schedule.html', {})