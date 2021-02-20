from home import Home
from registration.driver import Driver
from registration.rider import Rider
from utils.distance import Distance
from utils.fare import Fare

# this is a main method for application to call all the methods in code
if __name__ == "__main__":
    cabDriver = Driver() #object for driver
    cabRider = Rider()  #object for rider

    #launch home page
    Home().launch_home()
    
    #Driver registration code
    print("Registering Driver and Cab details")
    driverCount = int(input("Enter no of Drivers to Register: "))

    for _ in range(driverCount):
        name = input("Enter your Name:   ")
        cabno = input("Enter your Cab no:   ")
        contact = input("Enter Your  Mobile Number:  ")
        available = input("Enter <yes> if you are Available else <no>:  ")
        x1 = int(input("Enter Your Location Cordinate X:  "))
        x2 = int(input("Enter Your Location Cordinate Y:  "))

        driver_detail = cabDriver.register_driver(name, cabno, contact, available, x1, x2) 

        print("Registered Successfully:", driver_detail)
        
    #Rider registration code
    print("Registering Rider details")

    name = input("Enter Your Name:   ")
    city = input("Enter your city:   ")
    contact = input("Your Mobile Number Please:   ")
    booking = input("Enter <yes> if you want to book a ride:  ")
    y1 = int(input("Enter Your Location Cordinate X:  "))
    y2 = int(input("Enter Your Location Cordinate Y:  "))

    rider_detail = cabRider.register_rider(name, city, contact, booking, y1, y2)
    print("Your Details:", rider_detail)

    # history of both rider and driver for making data of history to display
    alldrivers = cabDriver.list_drivers()
    allriders = cabRider.list_ride_history()

    # to take the rider input
    cab_type = input("Please type cab type available <sedan> to book a ride:::   ")
    while cab_type != "sedan":
        print("Invalid selected car type.")
        cab_type = input("Please type cab type available <sedan> to book a ride:::   ")
        if cab_type == "sedan":
            break

    print("List of all cab/drivers avaiable: ", alldrivers)

    print("Please enter destination location to book a ride:")
    dest_x = int(input("enter x Coordinate:  "))
    dest_y = int(input("enter y Coordinate:  "))

    # to calculate the distance between driver and rider
    max_distance = 999
    assigned_Cab = None
    for driver in alldrivers:
        d = Distance().calculate_distance(driver["x1"], driver["x2"], rider_detail["y1"], rider_detail["y2"])
        print("This driver ", driver['name'], "is", d, "KM from you")
        if d < max_distance:
            max_distance = d
            assigned_Cab = driver
    print("Nearest driver/cab : ", assigned_Cab,
            "booked and will reach your location for pick up ")
    print("Enjoy your ride!!")

    # code for fare calculation
    fare_per_km = 5
    l = Fare().calculate_fare(rider_detail["y1"], rider_detail['y2'], dest_x, dest_y)
    print("Your destination has arrived!!")

    print("Total cost for trip to be paid is Rs.", l*fare_per_km)

while True:  # for implement function infinite times
    # prints are for information for next steps

    print("For Booking history of your rides, please type <history>:   ")
    print("To Exit, Please type <EXIT>:   ")

    # to take the rider input
    entry = input("Provide Your Input here:::   ")

    if entry == "history":  # for list data of rides taken
        print(allriders)

    if entry == "EXIT":  # for exit we using this function
        print("Thank you, visit again!!")
        break