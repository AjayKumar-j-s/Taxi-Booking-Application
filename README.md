Taxi Booking System
This repository contains a console-based Taxi Booking System implemented in Python. The system allows users to create taxis, book them based on availability and proximity, and view trip details and taxi earnings.

Features
Taxi Creation: Instantiates a specified number of taxis with unique IDs and default values for location and availability.
Taxi Booking: Books a taxi for a customer based on proximity and availability.
Trip Management: Logs trip details, calculates trip earnings, and updates the taxi's current location and availability.
Taxi and Trip Details: Prints detailed information about each taxi, including earnings, current spot, free time, and trip history.
Classes and Methods
Taxi Class

Attributes:

id: Unique identifier for each taxi.
booked: Booking status (boolean).
currentSpot: Current location of the taxi (e.g., A).
freeTime: Time when the taxi becomes free to take another booking.
totalEarnings: Total earnings of the taxi from completed trips.
trips: List of all trip details.
Methods:

setDetails(booked, currentSpot, freeTime, totalEarnings, tripDetail): Updates the taxi details after a booking.
printDetails(): Prints detailed trip history of the taxi.
printTaxiDetails(): Prints current status and earnings of the taxi.
Booking Class
Static Methods:
bookTaxi(customerID, pickupPoint, dropPoint, pickupTime, freeTaxis): Books a taxi for a customer and updates the taxi’s details.
createTaxis(n): Creates and returns a list of n taxis.
getFreeTaxis(taxis, pickupTime, pickupPoint): Filters and returns taxis available for booking based on pickup time and location.
main(): Entry point to interact with the booking system, providing options for booking and viewing details.
Usage
To use the system, run the main method in the Booking class:
Booking.main()
Commands
Once you start the program, you will see the following options:
Book Taxi:

Enter the Pickup Point (A-F).
Enter the Drop Point (A-F).
Enter the Pickup Time.
The program will automatically allocate the nearest available taxi.
Print Taxi Details:

View current status and total earnings for all taxis.
View detailed trip history of each taxi.
Example Interaction
plaintext
Copy code
0 -> Book Taxi
1 -> Print Taxi details

Enter choice: 0
Enter Pickup point: A
Enter Drop point: D
Enter Pickup time: 9
Taxi 1 booked

0 -> Book Taxi
1 -> Print Taxi details

Enter choice: 1
Taxi - 1 Total Earnings - 150 Current spot - D Free Time - 10
TaxiID    BookingID    CustomerID    From    To    PickupTime    DropTime    Amount
1               1          A      D       9          10           150


Requirements
Python 3.x
Run Instructions:
  Clone the repository.
  Run the code from your terminal:
  python3 taxi.py








