from django.shortcuts import render
from .models import Route, RouteTypes, RoutePoint, Stop


def main(request):
    buses = Route.objects.filter(type=RouteTypes.BUS)
    trolleybuses = Route.objects.filter(type=RouteTypes.TROLLEYBUS)

    return render(request, 'index.html', {'buses': buses, 'trolleybuses': trolleybuses})

def schedule(request):
    route = Route.objects.filter(code=request.GET['mar']).first()
    stops = RoutePoint.objects.filter(route=route)

    return render(request, 'schedule.html', {'stops': stops, 'type_m': route.type, 'mar_n': route.name, 'bus': RouteTypes.BUS, 'trolleybus': RouteTypes.TROLLEYBUS})

def bus_schedule(request):
    schedules = Stop.objects.filter(id=request.GET['stp']).first()
    mar_bs = Route.objects.filter(code=Route.code)

    return render(request, 'bus_schedule.html', {'schedules': schedules, 'mar_bs': mar_bs})