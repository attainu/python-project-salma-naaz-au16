import math

class Fare:

    def __init__(self, km_price= 5):
        self.per_km_fare = km_price

    def calculate_total_fare(self, trip_distance:int):
        return trip_distance*self.per_km_fare