import datetime
from intuginehelper import intuparser
import os
import sys

def get_diff(end, start):
    return (end - start).total_seconds()


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
        if len(trip_pings) <= 1:
            continue
        now_time = datetime.datetime.now()
        last_time = trip_pings[-1]['createdAt']
        ping_rate = intuparser.get_ping_rate(trip)
        time_diff = int(get_diff(now_time, last_time) * 100)
        if time_diff > ping_rate * float(os.environ['TIME_FACTOR']):
            res.append(trip_id)
    for x in res:
        print(str(x))
    print(len(res))


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
