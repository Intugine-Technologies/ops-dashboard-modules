import datetime
import sys
from intuginehelper import intuhelper


def main(trips, all_pings):
    # trips = intudb.get_running_trips()
    # all_pings = intudb.get_all_pings(trips)
    res = list()
    start_time = datetime.datetime.now() - datetime.timedelta(1)
    for trip in trips:
        trip_id = trip['_id']
        trip_pings = []
        for pings in all_pings:
            if pings['_id'] == trip_id:
                trip_pings = pings['pings']
        if len(trip_pings) <= 1:
            continue
        try:
            last_pings = list()
            for ping in trip_pings:
                ping_time = ping['createdAt']
                if ping_time > start_time:
                    last_pings.append(ping)
            total_dist = 0
            for i in range(len(last_pings) - 1):
                dist = intuhelper.get_distance(last_pings[i]['loc'], last_pings[i + 1]['loc'])
                total_dist += dist
            if total_dist < 200000:
                res.append(trip)
        except Exception as e:
            print(trip_id, e)
    print(res)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
