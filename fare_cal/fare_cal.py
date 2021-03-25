import math


def fare_cal(stations, fare_charge):
    if len(stations) <= 3:
        return 10
    else:
        return math.ceil(10+((len(stations))*fare_charge))
