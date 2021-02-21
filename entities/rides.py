class Rides:
    def __init__(self):
        self.rides = []

    def add_ride(self, rider_detail:dict, distance, fare):
        ride = {"rider": rider_detail, "trip_distance": distance, "trip_fare": fare}
        self.rides.append(ride)

    def list_ride_history(self):
        return self.rides