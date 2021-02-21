from registration.driver import Driver
from registration.rider import Rider
from entities.rides import Rides
from utils.distance import Distance
from utils.fare import Fare

class Application:

    def __init__(self):
        self.cab_driver = Driver() #object for driver
        self.cab_rider = Rider()  #object for rider
        self.rides = Rides() #object for rides

    #function to print welcome messages
    def launch_home(self):
        print("Welcome to Cab booking system")
        print("\n\n","Services available are :")
        self.print_services()
    
    def print_services(self):
        print(" 1. Register Driver \n",
                "2. Register Rider \n",
                "3. Book Cab & Ride \n",
                "4. Check Ride History \n",
                "5. Switch On/Off Driver Avaiability \n",
                "6. Update Cab's Location \n",
                "7. Exit: \n")

    #function to register driver
    def register_drivers(self):
        print("Registering Driver and Cab details")
        driver_count = int(input("Enter no of Drivers to Register, default = <1>: ") or 1)

        for _ in range(driver_count):
            self.register_driver()
    
    def register_driver(self):
        name = input("Enter your Name:   ")
        cabno = input("Enter your Cab no:   ")
        contact = input("Enter Your  Mobile Number:  ")
        available = input("Enter <yes> if you are Available else <no>:  ") or "yes"
        x = int(input("Enter Your Location Cordinate X:  ") or 100)
        y = int(input("Enter Your Location Cordinate Y:  ") or 200)

        driver_detail = self.cab_driver.register_driver(name, cabno, contact, available, x, y) 
        print("\n\n","Driver Registered Successfully:", driver_detail)
        return driver_detail

    def register_rider(self):
        print("Registering Rider details")
        name = input("Enter Your Name:   ")
        city = input("Enter your city:   ")
        contact = input("Your Mobile Number Please:   ")
        x = int(input("Enter Your Location Cordinate X:  ") or 100)
        y = int(input("Enter Your Location Cordinate Y:  ") or 200)

        rider_detail = self.cab_rider.register_rider(name, city, contact, x, y)
        print("\n\n","Rider Registered Successfully :", rider_detail)
        return rider_detail

    #function for booking a cab/ride
    def ride(self, rider_detail):
        print('\n'*2)
        cab_type = input("Please type cab type available <sedan> to book a ride:::   ")
        while cab_type != "sedan":
            print("Invalid selected car type.")
            cab_type = input("Please type cab type available <sedan> to book a ride:::   ")

        print("Please enter destination location to book a ride:")
        dest_x = int(input("enter x Coordinate:  "))
        dest_y = int(input("enter y Coordinate:  "))

        assigned_cab = self.find_nearest_cab(rider_detail)
        if not assigned_cab:
            print("\n\n","No cabs available right now. Please try later")
        else:

            #book cab and mark unavailable till ride completes
            self.book_cab(assigned_cab)

            #Print Trip/Ride Messages
            print("\n\n","Enjoy your ride!!")
            print("You have reached your destination")

            trip_distance = self.calc_distance(rider_detail["x"], rider_detail["y"], dest_x, dest_y)
            print('\n' *2, "Your Trip Distance is: ", trip_distance)

            #End Trip/ride
            total_fare = self.calc_trip_fare(rider_detail, dest_x, dest_y)
            print("\n\n","Total cost for trip to be paid is Rs.", total_fare)

            #Release cab by making it available and update current location
            self.release_cab(assigned_cab, dest_x, dest_y)

            self.rides.add_ride(rider_detail, trip_distance, total_fare)

    # function to find nearest cab available
    def find_nearest_cab(self, rider_detail):
        all_drivers = self.cab_driver.list_drivers()
        print("\n\n","List of all cab/drivers avaiable: ", all_drivers)
        max_distance = 999
        assigned_Cab = None
        for driver in all_drivers:
            if(driver["available"].lower() == 'yes'):

                source_x = driver["x"]
                source_y = driver["y"]
                dest_x = rider_detail["x"]
                dest_y = rider_detail["y"]

                d = self.calc_distance(source_x, source_y, dest_x, dest_y)
                print("\n\n","This driver ", driver['name'], "is", d, "KM from you")

                if d < max_distance:
                    max_distance = d
                    assigned_Cab = driver  
        return assigned_Cab  
    
    # function for fare calculation
    def calc_trip_fare(self, rider_detail, dest_x, dest_y):
        fare_per_km = 5
        source_x = rider_detail["x"]
        source_y = rider_detail["y"]
        f = Fare()
        fare = f.calculate_fare(source_x, source_y, dest_x, dest_y)
        print("\n\n","Your destination has arrived!!")
        total_fare = fare*fare_per_km
        return total_fare

    def calc_distance(self, source_x, source_y, dest_x, dest_y):
        d = Distance()
        total_distance = d.calculate_distance(source_x, source_y, dest_x, dest_y)
        return total_distance

    def print_ride_history(self):
        print("\n\n", self.rides.list_ride_history())
    
    def print_rider_driver_data(self):
        print("List of all Drivers and Riders are :")
        print("\n\n",self.cab_driver.list_drivers())
        print(self.cab_rider.list_riders())

    #function to block cab for not sharing with other rides till trip completes
    def book_cab(self, cab_details):
        print("\n\n","Nearest driver/cab : ",cab_details,
                    "booked and will reach your location for pick up ")
        self.cab_driver.switch_on_off_driver(cab_details, "no")
    
    #function to release cab and update new location after completing trip
    def release_cab(self, cab_details, loc_x, loc_y):
        print("Releasing cab")
        self.cab_driver.switch_on_off_driver(cab_details, "yes")
        self.cab_driver.update_cab_location(cab_details, loc_x, loc_y)
    
    def update_driver_availability(self, driver_name, available):
        all_drivers = self.cab_driver.list_drivers()
        valid_driver = False
        for driver in all_drivers:
            if driver["name"].lower() == driver_name.lower():
                self.cab_driver.switch_on_off_driver(driver, available)
                valid_driver = True
                break
        if not valid_driver:
            print("Invalid Driver Name, Please enter valid driver name registered")

    def update_cab_location(self, driver_name, loc_x:int, loc_y:int):
        all_cabs = self.cab_driver.list_drivers()
        valid_driver = False
        for cab in all_cabs:
            if cab["name"].lower() == driver_name.lower():
                self.cab_driver.update_cab_location(cab, loc_x, loc_y)
                valid_driver = True
                break
        if not valid_driver:
            print("Invalid Driver Name, Please enter valid driver name registered")



