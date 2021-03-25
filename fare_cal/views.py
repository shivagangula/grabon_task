from django.shortcuts import render, HttpResponse
from .models import LineDetail, BoardingDetail
from .const import BLUE
import json

from .stations import find_stations_between
from .fare_cal import fare_cal


def test(request):

    if request.method == 'GET':
        return render(request, 'fare_cal/fare.html', {'request_type': 'get'})
    else:
        p1 = request.POST['from_name']
        p2 = request.POST['to_name']
        stations_between, fare_charge = find_stations_between(p1, p2)
        fare = fare_cal(stations_between, fare_charge)
        return render(request, 'fare_cal/fare.html', {'request_type': 'post',
                                                      'bs': stations_between,
                                                      'fare': fare})


def boarding_names_ajex(request):
    if request.method == 'GET':
        if request.is_ajax():
            ajex_word = request.GET.get('term', '').capitalize()
            search_qs = BoardingDetail.objects.filter(
                boarding_name__istartswith=ajex_word)
            results = []
            for inst in search_qs:
                out = inst.boarding_name
                results.append(out)
            results = list(dict.fromkeys(results))
            data = json.dumps(results)
        else:
            data = 'fail'
        mimetype = 'application/json'
        return HttpResponse(data, mimetype)
