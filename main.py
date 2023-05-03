# Aaron Anguiano Student ID: 001307831
import datetime
from MakeHashTable import MakeHashTable
from ReadCSVs import ReadCSVs
from Truck import truckNumberOne, truckNumberTwo, truckNumberThree

# initialize the ReadCSV class
readCSVs = ReadCSVs()

# use the getPackages method to retrieve all
# packages and assign it to a variable
allPkgs = readCSVs.getPackages()

# these package ids are determined based
# on the instructions and special notes
# in the packages.csv file
truck1Ids = [1, 13, 14, 15, 16, 20, 29, 30, 31, 34, 37, 40]
truck2Ids = [3, 6, 12, 17, 18, 19, 21, 22, 23, 24, 26, 27, 35, 36, 38, 39]
truck3Ids = [2, 4, 5, 6, 7, 8, 9, 10, 11, 25, 28, 32, 33]

# initialize a hash table
# and give it a length of size
# of the allPkgs array
packageHashTable = MakeHashTable(len(allPkgs))

# add each package to the hash table using
# the add method of MakeHashTable
for package in allPkgs:
    hashKey = package.packageID
    packageHashTable.add(hashKey, package)


# Giving the trucks their proper
# package IDs.
truckNumberOne.packageIdArray = truck1Ids
truckNumberTwo.packageIdArray = truck2Ids
truckNumberThree.packageIdArray = truck3Ids


# nearest neighbor algo to determine the
# stops for the trucks
def delivery(truck):
    undeliveredIds = truck.packageIdArray
    truck.newPackageOrder = []
    # starts a while loop that continues to loop
    # for as long as undeliveredIds is empty
    while undeliveredIds:
        # large initial value to start the loop. is only used for
        # the first package
        nextAddressDistance = 9999
        # this value changes when we find a new closest
        # package in the loop.
        nextPackage = None
        # for loop that checks every undelivered package
        # then puts in the address of the truck and the
        # package to check the distance in distances.csv
        for innerPackageId in undeliveredIds:
            innerPack = packageHashTable.get(innerPackageId)
            truckAddress = readCSVs.getAddressIndex(truck.address)
            packAddress = readCSVs.getAddressIndex(innerPack.packageAddress)
            truckPackDistance = readCSVs.getDistances(truckAddress, packAddress)
            if truckPackDistance <= nextAddressDistance:
                nextAddressDistance = truckPackDistance
                nextPackage = innerPack
        # once the nearest package destination is found,
        # the id is added to a new property
        truck.newPackageOrder.append(nextPackage.packageID)
        # the ID is removed from undeliveredIds so that
        # the loop doesn't run forever.
        undeliveredIds.remove(nextPackage.packageID)
        truck.miles = truck.miles + nextAddressDistance
        truck.address = nextPackage.packageAddress
        # dividing the distance by 18 as per the instructions
        # the truck is going a speed of 18 MPH
        truck.time = truck.time + datetime.timedelta(hours=nextAddressDistance / 18)
        nextPackage.packageDeliveryTime = truck.time
        nextPackage.packageDeparture = truck.departureTime


delivery(truckNumberOne)
delivery(truckNumberTwo)

# there are only two drivers. so after the first truck
# finishes, the driver moves to the new truck.
if truckNumberOne.time < truckNumberTwo.time:
    truckNumberThree.departureTime = truckNumberOne.time
else:
    truckNumberThree.departureTime = truckNumberTwo.time

delivery(truckNumberThree)

newPackageDetails = truckNumberOne.newPackageOrder + truckNumberTwo.newPackageOrder + truckNumberThree.newPackageOrder
packageDetails = truckNumberOne.packageIdArray + truckNumberTwo.packageIdArray + truckNumberThree.packageIdArray
totalMiles = truckNumberOne.miles + truckNumberTwo.miles + truckNumberThree.miles


print("Welcome to the WGUPS Terminal Tracking Application")
msg = "Please enter the ID of the package you would like to track. If you would like to see the status of all " \
      "packages, enter 'all' "
text = input(msg).capitalize()
if text == 'All':
    try:
        timeQuestion = "At what time would you like to see the status of all packages? Please format the time as HH:MM. "
        timeText = input(timeQuestion)
        (timeHour, timeMin) = timeText.split(":")
        timeHourInt = int(timeHour)
        timeMinInt = int(timeMin)
        timeSelected = datetime.timedelta(hours=timeHourInt, minutes=timeMinInt)
        newPackageDetails.sort()
        for packageId in newPackageDetails:
            pack = packageHashTable.get(packageId)
            if pack.packageDeliveryTime < timeSelected:
                pack.packageStatus = "Delivered"
            elif pack.packageDeparture > timeSelected:
                pack.packageStatus = "En Route"
            else:
                pack.status = "At The Hub"
            pack.printPackageDetails()

    except ValueError:
        print("Please Format your time correctly.")
else:
    try:
        selectedId = int(text)
        if selectedId > len(newPackageDetails) or selectedId < 1:
            print("The Package ID you entered is invalid. Please try Again.")
            exit()
        timeQuestion = "At what time would you like to see the status of your package? Please format the time as HH:MM"
        timeText = input(timeQuestion)
        (timeHour, timeMin) = timeText.split(":")
        timeHourInt = int(timeHour)
        timeMinInt = int(timeMin)
        timeSelected = datetime.timedelta(hours=timeHourInt, minutes=timeMinInt)
        try:

            selectedPackage = packageHashTable.get(selectedId)
            if selectedPackage.packageDeliveryTime < timeSelected:
                selectedPackage.packageStatus = "Delivered"
            elif selectedPackage.packageDeliveryTime > timeSelected:
                selectedPackage.packageStatus = "En Route"
            else:
                selectedPackage.packageStatus = "At Hub"
            selectedPackage.printPackageDetails()
        except ValueError:
            print("Please enter a valid ID")

    except ValueError:
        print("Please enter a time in the format HH:MM.")

print("The total amount of miles for all deliveries is " + str(totalMiles))
exit()
