
### pre requirements

|Key|Value|
|---|---|
|`DATABASE_SERVER`| `server link` |
|`DATABASE_CLIENT`| `telenitytracking` |
|`BLACKLIST_CLIENTS`| separated by comma |
|`BLACKLIST_CLIENT_CLIENT`| separated by comma |
|`ETA_TIME_FACTOR`| `3.14` |
|`TIME_FACTOR`|`foro stopped in midway`|
|`DIST_THRESHOLD`| `trips not in motion distance threshold in meters` |

## Battery Percentage

Prints battery percentage

> voltage between 3.65 to 4.2  

    python3 battery_percenatge.py voltage
    python3 battery_percenatge.py 3.9
    
## late trips

Prints a list of all the late trips 

    python3 late_trips.py tripsObject
    
## Stopped in Midway
prints all the tripId's that are stopped in midway

    python3 stopped_in_midway.py tripsObject all_pings_for_trips
    
## Trips not in motion

prints Object of all the trips that are not in motion

    python3 trips_not_in_motion.py tripsObject all_pings_for_trips
    
## Unusual Haults

print an Object of all the trips having unusual haults

    python3 unusual_haults.py tripsObject all_pings_for_trips
    
    
### TripsObject

```json5
[
  {
      "_id": "ObjectId('')",
      "etc" : "etc"
  }
]
```

### all_pings_for_trips


```json
[ 
  {
    "_id":"tripId", 
    "pings": ["Object(ping1)", "Object(ping2)"]
  }
]
```