import csv
from Package import Package


class ReadCSVs:
    def __init__(self):
        return

# returns an array of packages
# reads from the packages.csv file
    def getPackages(self):
        allPackages = []
        # use csv reader to go row by row
        # assign each cell in that row as a variable
        with open("packages.csv") as packages:
            packageInfo = csv.reader(packages)
            for package in packageInfo:
                pId = int(package[0])
                pAddy = package[1]
                pCity = package[2]
                pState = package[3]
                pZip = package[4]
                pDeadline = package[5]
                pWeight = package[6]

            # create a new package from the variables.
                newPackage = Package(pId, pAddy, pCity, pState, pZip, pDeadline, pWeight, "at the hub")
            # add this new package to the allPackages variable
                allPackages.append(newPackage)
        return allPackages

    def getDistances(self, col, row):
        with open("distances.csv") as distancesCSV:
            csvDist = csv.reader(distancesCSV)
            csvDist = list(csvDist)
        if csvDist[col][row] == '':
            return float(csvDist[row][col])
        return float(csvDist[col][row])

    def getAddressIndex(self, address):
        with open("addresses.csv") as addressCSV:
            csvAddress = csv.reader(addressCSV)
            csvAddress = list(csvAddress)
        for row in csvAddress:
            if address in row[2]:
                return int(row[0])

