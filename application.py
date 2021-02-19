from registerdriver import Driver

from registerrider import Rider

# this is a main method for application to call all the methods in code
if __name__ == "__main__":
    cabDriver = Driver() #object for driver
    cabRider = Rider()  #object for rider

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

        driverDetails = cabDriver.register_driver(name, cabno, contact, available, x1, x2) 

        print("Registered Drivers:", driverDetails)
        cabDriver.list_drivers()
    #Rider registration code
    print("Registering Rider details")

    name = input("Enter Your Name:   ")
    city = input("Enter your city:   ")
    contact = input("Your Mobile Number Please:   ")
    booking = input("Enter <yes> if you want to book a ride:  ")
    y1 = int(input("Enter Your Location Cordinate X:  "))
    y2 = int(input("Enter Your Location Cordinate Y:  "))

    riderDetails = cabRider.register_rider(name, city, contact, booking, y1, y2)
    print("Your Details:", riderDetails)

