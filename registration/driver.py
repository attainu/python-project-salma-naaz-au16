# Class For register and get the cab driver data
from database.data import DataStore

class Driver:
    def __init__(self):
        self.data_file = DataStore()
        self.drivers = []

    def register_driver(self, name, cabno, contact, available, x:int, y:int):
        driver_details = {"name": name, "cabno": cabno, "contact": contact,
                   "available": available, "x": x, "y": y}
        self.data_file.write_driver_info(driver_details)
        self.drivers.append(driver_details)
        return driver_details
    
    def list_drivers_from_db(self):
        return self.data_file.read_driver_info()

    def list_drivers(self):
        return self.drivers

    def update_cab_location(self, driver:dict, loc_x:int, loc_y:int):
        print("Updating Cab's new location : X =", loc_x, "Y =", loc_y)
        updated_location = {"x" : loc_x, "y": loc_y}
        driver.update(updated_location)

    def switch_on_off_driver(self, driver:dict, available):
        print("Updating Cab's availability as :", available)
        updated_availability = {"available" : available}
        driver.update(updated_availability)
