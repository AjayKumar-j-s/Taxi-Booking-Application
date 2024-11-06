class Taxi:
    taxicount = 0  # Static variable for taxi number

    def __init__(self):
        self.id = Taxi.taxicount + 1
        self.booked = False
        self.currentSpot = 'A'  # Start point A
        self.freeTime = 6  # Example: 6 AM
        self.totalEarnings = 0
        self.trips = []  # List to store trip details
        Taxi.taxicount += 1  # Increment taxi count for unique id

    def setDetails(self, booked, currentSpot, freeTime, totalEarnings, tripDetail):
        self.booked = booked
        self.currentSpot = currentSpot
        self.freeTime = freeTime
        self.totalEarnings = totalEarnings
        self.trips.append(tripDetail)

    def printDetails(self):
        print(f"Taxi - {self.id} Total Earnings - {self.totalEarnings}")
        print("TaxiID    BookingID    CustomerID    From    To    PickupTime    DropTime    Amount")
        for trip in self.trips:
            print(f"{self.id}          {trip}")
        print("--------------------------------------------------------------------------------------")

    def printTaxiDetails(self):
        print(f"Taxi - {self.id} Total Earnings - {self.totalEarnings} Current spot - {self.currentSpot} Free Time - {self.freeTime}")


class Booking:
    @staticmethod
    def bookTaxi(customerID, pickupPoint, dropPoint, pickupTime, freeTaxis):
        min_distance = 999
        distanceBetweenpickUpandDrop = 0
        earning = 0
        nextfreeTime = 0
        nextSpot = 'Z'
        bookedTaxi = None
        tripDetail = ""

        for t in freeTaxis:
            distanceBetweenCustomerAndTaxi = abs(ord(t.currentSpot) - ord(pickupPoint)) * 15
            if distanceBetweenCustomerAndTaxi < min_distance:
                bookedTaxi = t
                distanceBetweenpickUpandDrop = abs(ord(dropPoint) - ord(pickupPoint)) * 15
                earning = (distanceBetweenpickUpandDrop - 5) * 10 + 100
                dropTime = pickupTime + distanceBetweenpickUpandDrop // 15
                nextfreeTime = dropTime
                nextSpot = dropPoint
                tripDetail = (f"{customerID}               {customerID}          {pickupPoint}      {dropPoint}       "
                              f"{pickupTime}          {dropTime}           {earning}")
                min_distance = distanceBetweenCustomerAndTaxi

        bookedTaxi.setDetails(True, nextSpot, nextfreeTime, bookedTaxi.totalEarnings + earning, tripDetail)
        print(f"Taxi {bookedTaxi.id} booked")

    @staticmethod
    def createTaxis(n):
        return [Taxi() for _ in range(n)]

    @staticmethod
    def getFreeTaxis(taxis, pickupTime, pickupPoint):
        freeTaxis = []
        for t in taxis:
            if t.freeTime <= pickupTime and abs(ord(t.currentSpot) - ord(pickupPoint)) <= pickupTime - t.freeTime:
                freeTaxis.append(t)
        return freeTaxis

    @staticmethod
    def main():
        taxis = Booking.createTaxis(4)
        id = 1

        while True:
            print("0 - > Book Taxi")
            print("1 - > Print Taxi details")
            choice = int(input())

            if choice == 0:
                customerID = id
                pickupPoint = input("Enter Pickup point: ").strip().upper()[0]
                dropPoint = input("Enter Drop point: ").strip().upper()[0]
                pickupTime = int(input("Enter Pickup time: "))

                if pickupPoint < 'A' or dropPoint > 'F' or pickupPoint > 'F' or dropPoint < 'A':
                    print("Valid pickup and drop are A, B, C, D, E, F. Exiting")
                    return

                freeTaxis = Booking.getFreeTaxis(taxis, pickupTime, pickupPoint)

                if not freeTaxis:
                    print("No Taxi can be allotted. Exiting")
                    return

                freeTaxis.sort(key=lambda x: x.totalEarnings)
                Booking.bookTaxi(id, pickupPoint, dropPoint, pickupTime, freeTaxis)
                id += 1

            elif choice == 1:
                for t in taxis:
                    t.printTaxiDetails()
                for t in taxis:
                    t.printDetails()
            else:
                return


# To run the main function
Booking.main()
