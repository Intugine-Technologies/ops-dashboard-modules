from intuginehelper import intuginehelper, intuparser
from datetime import datetime, timedelta
import os
import sys

def main(trips):
    print(len(trips))
    res = list()
    for trip in trips:
        eta_hrs = intuginehelper.get_eta_hrs(trip)
        eta_hrs = float(os.environ['ETA_TIME_FACTOR']) * eta_hrs
        start_time = intuparser.get_createdAt(trip)
        start_time = start_time + timedelta(hours=eta_hrs)
        if start_time >= datetime.now():
            res.append(trip)
    print(res)


if __name__ == '__main__':
    main(sys.argv[1])
