
#model for Packages.
# the properties for this model were determined
# by the details in section F.
class Package:
    def __init__(self, packageID, packageAddress, packageCity, packageState, packageZipCode, packageDeadline, packageWeight, packageStatus):
        self.packageID = packageID
        self.packageAddress = packageAddress
        self.packageCity = packageCity
        self.packageState = packageState
        self.packageZipCode = packageZipCode
        self.packageDeadline = packageDeadline
        self.packageWeight = packageWeight
        self.packageStatus = packageStatus
        self.packageDeparture = None
        self.packageDeliveryTime = None

# prints out the package details in a more readable format.
    def printPackageDetails(self):
        print("Package ID: " + str(self.packageID) + " // Address: " + self.packageAddress + " " + self.packageCity + ", " + self.packageState + " " + self.packageZipCode + " // Deadline: " + self.packageDeadline + " // Weight: " + self.packageWeight + " // Status: " + self.packageStatus + " // Departure Time: " + str(self.packageDeparture) + " // Delivery Time: " + str(self.packageDeliveryTime))


