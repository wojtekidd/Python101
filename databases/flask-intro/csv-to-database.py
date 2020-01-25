from models import *
import csv

db.create_all()

with open('flights.csv', 'r') as f:
    reader = csv.reader(f)

    for ori, des, dur in reader:
        db.session.add(Flights(origin=ori, destination=des, duration=dur))
        print(f"Flight from {ori} to {des} added")


with open('passengers.csv', 'r') as p:
    reader = csv.reader(p)

    for name, flight_id in reader:
        db.session.add(Passengers(name=name, flight_id=flight_id))
        print(f"Added passenger {name}, to flight {flight_id}")

db.session.commit()
