import datetime
import os
from intuginehelper import intuhelper
import sys


gmt_to_ist = datetime.timedelta(hours=5, minutes=30)


def main(trips, all_pings):
    # trips = intudb.get_running_trips()
    # all_pings = intudb.get_all_pings(trips)
    res = list()
    for trip in trips:
        trip_id = trip['_id']
        trip_pings = []
        for pings in all_pings:
            if pings['_id'] == trip_id:
                trip_pings = pings['pings']
        if len(trip_pings) <= 2:
            continue
        try:
            start_loc = trip_pings[0]['loc']
            start_time = trip['createdAt']
            if isinstance(start_time, str):
                continue
        except Exception as e:
            print(e)
            continue
        if gmt_to_ist + start_time + datetime.timedelta(1) >= datetime.datetime.now():
            continue
        ok = True
        for now in trip_pings[1:]:
            now_loc = now['loc']
            dist = intuhelper.get_distance(start_loc, now_loc)
            if dist >= int(os.environ['DIST_THRESHOLD']):
                ok = False
        if ok:
            res.append(trip)
    print(res)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
