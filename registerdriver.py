# Class For register and get the cab driver data
from data import DataStore

class Driver:
    def __init__(self):
        self.drivers = []
        self.data_file = DataStore()

    def register_driver(self, name, cabno, contact, available, location_x, location_y):
        driver_details = {"name": name, "cabno": cabno, "contact": contact,
                   "available": available, "x1": location_x, "x2": location_y}
        self.drivers.append(driver_details)
        self.data_file.write_driver_info(driver_details)
        return driver_details
    
    def list_drivers(self):
        print(self.data_file.read_driver_info)
        return self.drivers