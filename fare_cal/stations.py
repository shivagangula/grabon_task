from .const import BLUE, LOOP
import itertools
from .models import LineDetail, BoardingDetail


def find_stations_between(p1, p2):
    avai_lits = []
    for paths in itertools.chain(BLUE, LOOP):
        try:
            if p1 in paths and p2 in paths:
                avai_lits.append(paths)
        except:
            raise ValueError
    try:
        stations = min(avai_lits)
        p1_index = stations.index(p1)
        p2_index = stations.index(p2)
        fare_charge = BoardingDetail.objects.get(
            boarding_name=p1).line_details.line_charge

        if len(stations[p1_index:p2_index]) != 0:
            return_list = stations[p1_index:p2_index]

        else:
            return_list = stations[p2_index:p1_index]

    except:
        return_list = ['Please Select Stations Between ']
        fare_charge = 0
    return return_list, fare_charge
