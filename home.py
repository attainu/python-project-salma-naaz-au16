def launch_home():
        print("Welcome to Cab booking system")
        print("Please select services available : ")
        services = "1.Book Cab & Ride \n 2.Driver & Cab Registration \n 3. Rider Registration \n 4. Check History of Rides \n 5. Exit:"
        operation = int(input(services))

        if operation == 1:
            print("please register the cabs available")
        elif operation == 2:

