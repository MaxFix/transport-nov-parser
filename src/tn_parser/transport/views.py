from django.shortcuts import render
from .models import Route, RouteTypes, RoutePoint, EnumBase


def main(request):
    buses = Route.objects.filter(type=RouteTypes.BUS)
    trolleybuses = Route.objects.filter(type=RouteTypes.TROLLEYBUS)

    return render(request, 'index.html', {'buses': buses, 'trolleybuses': trolleybuses})

def schedule(request):
    route = Route.objects.filter(code=request.GET['mar']).first()
    stops = RoutePoint.objects.filter(route=route)

    return render(request, 'schedule.html', {'stops': stops, 'type_m': route.type, 'mar_n': route.name, 'bus' : RouteTypes.BUS, 'trolleybus' : RouteTypes.TROLLEYBUS})

def bus_schedule(request):
    return render(request, 'bus_schedule.html', {})