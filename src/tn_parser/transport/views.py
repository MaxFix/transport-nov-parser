from django.http import Http404, HttpResponse
from django.shortcuts import render
from .models import Route, RouteTypes, RoutePoint, Stop
from django.core.exceptions import ObjectDoesNotExist


def main(request):
    buses = Route.objects.filter(type=RouteTypes.BUS)
    trolleybuses = Route.objects.filter(type=RouteTypes.TROLLEYBUS)

    return render(request, 'index.html', {'buses': buses, 'trolleybuses': trolleybuses})

def schedule(request):
    # if not len(request.GET):            Проверка заполненности
    #     return HttpResponse('non')
    try:
        route = Route.objects.get(code=request.GET['mar'])
        stops = RoutePoint.objects.filter(route=route)
    except ObjectDoesNotExist:
        raise Http404('Не найден маршрут')
    except KeyError:
        raise Http404('Не найден параметр маршрута')

    return render(request, 'schedule.html', {'stops': stops, 'type_m': route.type, 'mar_n': route.name, 'bus': RouteTypes.BUS, 'trolleybus': RouteTypes.TROLLEYBUS, 'mar': request.GET['mar']})

#добавить исключение некорректного и пустого запроса
#корректное получение get запроса

def bus_schedule(request):
    try:
        stop = Stop.objects.get(id=request.GET['stp'])
        mar_bs = Route.objects.filter(code=request.GET['mar'])
        mar_time = RoutePoint.objects.filter(route= mar_bs,stop= stop)
        route = Route.objects.get(code=request.GET['mar'])
    except ObjectDoesNotExist:
        raise Http404('Не найдена остановка')
    except KeyError:
        raise Http404('Не найден параметр остановки')

    return render(request, 'bus_schedule.html', {'schedules': mar_time, 'mar_bs': mar_bs, 'mar_time': mar_time, 'mar_n': route.name})