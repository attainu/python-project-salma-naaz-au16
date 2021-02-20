# Class For register and get the rider data
from database.data import DataStore
class Rider:
    def __init__(self):
        self.data_file = DataStore()
        
    def register_rider(self, name, location, phone_no, booking, location_x, location_y):
        rider = {"name": name, "location": location, "phone_no": phone_no, "booking": booking,
                 "y1": location_x, "y2": location_y}
        self.data_file.write_rider_info(rider)
        return rider

    def list_ride_history(self):
        return self.data_file.read_rider_info()