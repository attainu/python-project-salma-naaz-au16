# Cab Booking System
This Application is a cab booking platform to allow a rider to book a cab.

## Usage
Clone this Repository and execute main.py, which will pop for input choices
and choosing operations to be performed.

## Features of this code
```
* Register a rider
* Register a driver/cab
* A rider can book a cab
* Update a cab's location
* A driver can switch on/off his availability
* Fetch history of all rides taken by a rider
* End the Trip
```

## Extra/Extended Features 
```
* Calculate Trip Distance and Total Fare
* Display Fare and trip distance in ride history
* Storing rider and driver data to file using Pickle
```

### Customizability in Command-Line Parameters
Some of the command line parameters have default values like 
```
1. No of drivers
2. Current location
3. default operation for exit
etc.
```

### Execution Flow-
First it will register driver , rider and book a cab with calculating distance and fare. 
After first booking application will allow user to give choices and perform 
required operation untill """EXIT""" is selected

#### Some important things used in project
Used Picke module to store data into file and read from file. 
Distance calcuation to find the nearest available cab.
Fare calculation based on source and destination with fare per KM.
Identifying driver by driver name to update location and availability.

#### Future improvements:
We can design an user interface for the program so a normal user can easily
interact with it. We can add more features like displaying different types of cabs and sharing rides between different riders.