from main import Flight, TravelPlanner
import argparse
from datetime import  datetime
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="This script is for flights")
    parser.add_argument("creat_flight", nargs=4, help="Is for adding flights")
    parser.add_argument("-d", "--duration", type=int, help="getting flight number")

    args = parser.parse_args()

    if args.duration:
        for flight in TravelPlanner.flights:
            if flight.flight_number == args.duration:
                print(flight.get_flight_duration())
    departure = args.creat_flight[0]
    destination = args.creat_flight[1]
    departure_time = datetime.strptime(args.creat_flight[2], "%Y-%m-%d %H:%M:%S")
    destination_time = datetime.strptime(args.creat_flight[3], "%Y-%m-%d %H:%M:%S")
    flight = Flight(departure, destination, departure_time, destination_time)
    TravelPlanner.add_flight(flight)
# python script.py -d 1
