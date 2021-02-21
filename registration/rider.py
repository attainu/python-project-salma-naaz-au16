# Class For register and get the rider data
from database.data import DataStore
class Rider:
    def __init__(self):
        self.data_file = DataStore()
        self.riders = []
        
    def register_rider(self, name, location, phone_no, location_x, location_y):
        rider = {"name": name, "location": location, "phone_no": phone_no,
                 "x": location_x, "y": location_y}
        self.data_file.write_rider_info(rider)
        self.riders.append(rider)
        return rider

    def list_riders(self):
        return self.riders
    
    def list_rider_history_from_db(self):
        return self.data_file.read_rider_info()