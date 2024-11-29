from datetime import datetime


class Flight:
    counter = 0

    def __init__(self, departure, destination, departure_time, arrival_time):
        self.departure = departure
        self.destination = destination
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.flight_number = Flight.counter
        Flight.counter += 1

    def get_flight_duration(self):
        duration = self.arrival_time - self.departure_time
        return duration

    def format_flight_time(self):
        formatted_departure_time = self.departure_time.strftime("%Y-%m-%d %H:%M:%S")
        formatted_arrival_time = self.arrival_time.strftime("%Y-%m-%d %H:%M:%S")
        return f" arrival time is: {formatted_arrival_time}, departure time is: {formatted_departure_time}"

class TravelPlanner:
    flights = []
    # flight = [flight1, flight2, ...]
    @classmethod
    def add_flight(cls, flight):
        cls.flights.append(flight)
    @classmethod
    def sorting_flights(cls):
        sorted_flights = list(sorted(cls.flights, key=lambda _flight: _flight.departure_time))
        return sorted_flights
    @classmethod
    def total_travel_time(cls):
        total_duration = 0
        for flight in cls.flights:
            total_duration += flight.get_flight_duration()
        return total_duration
