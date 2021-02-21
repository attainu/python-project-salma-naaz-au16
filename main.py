from application.app import Application

if __name__ == "__main__":
    app = Application() #object for application
    
    #Launch home to display welcome messages
    app.launch_home()

    #Driver registration
    app.register_drivers()

    #Rider registration
    rider_detail = app.register_rider()

    #Print Rider and Driver details
    app.print_rider_driver_data()

    #Book a ride
    app.ride(rider_detail)

    while True:  # for implement function infinite times

        print("\n\nPlease select your choice below for services",
                "leave empty to exit application")
        app.print_services()
        operation = int(input() or 7)

        if operation == 1: # register driver
            driver_detail = app.register_driver()
        
        elif operation ==2: #register rider
            rider_detail = app.register_rider()

        elif operation == 3: # to book a cab with existing rider or new rider
            if not rider_detail:
                print("No Riders Registered, Please register a rider")
            else:
                app.ride(rider_detail)

        elif operation == 4: # To print ride history
            app.print_ride_history()

        elif operation == 5: # switch on/off driver availability
            driver_name = input("Please enter Driver name :")
            driver_availability = input("Please enter Driver availability :")
            app.update_driver_availability(driver_name, driver_availability)

        elif operation == 6: # update cab location
            driver_name = input("Please enter Driver name :")
            loc_x = int(input("Please enter new location X :"))
            loc_y = int(input("Please enter new location Y :"))
            app.update_cab_location(driver_name, loc_x, loc_y)

        elif operation == 7:  # To Exit
            print("\n\n","Thank you, visit again!!")
            break
            
        else:
            print("Please select valid choice from the services available")