class Rider:
    def __init__(self):
        self.riders = []
        
    def register_rider(self, name, location, phone_no, booking, location_x, location_y):
        rider = {"name": name, "location": location, "phone_no": phone_no, "booking": booking,
                 "y1": location_x, "y2": location_y}
        self.riders.append(rider)
        return rider

    def list_ride_history(self):
        return self.riders