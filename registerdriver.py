# Class For register and get the cab driver data
class Driver:
    def __init__(self):
        self.drivers = []

    def register_driver(self, name, cabno, contact, available, location_x, location_y):
        driver_details = {"name": name, "cabno": cabno, "contact": contact,
                   "available": available, "x1": location_x, "x2": location_y}
        self.drivers.append(driver_details)
        return driver_details
    
    def list_drivers(self):
        return self.drivers