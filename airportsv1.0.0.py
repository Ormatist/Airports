# imports csv module
import csv
from re import I

# opens the csv file
file = open("Airports.csv")

# sets csvreader to all values in csv file
csvreader = csv.reader(file)

# initiates the rows list
rows  = []

# for each row in the file
for row in csvreader:

    # add that row to the rows list
    rows.append(row)

# closes file
file.close()

# defines the planes nested list
planes =[["Medium narrow body","£8","2650","180","8"],["Large narrow body","£7","5600","220","10"],["Medium wide body","£5","4050","406","14"]]

# defines the options subroutine
def options():
    
    # Ensures the variables are made global for later use 
    global ukCode
    global overseasCode
    
    # defines the airport details subroutine
    def airportDetails():
        
        ukCode = None
        overseasCode = None
        # sets the variable ukCode to the user input
        ukCode = input("##############################################\nPlease enter the 3 letter UK Airport code\n##############################################\n")

        # if airport code is either BOH or LPL
        if ukCode == "BOH" or ukCode == "LPL":
            # sets over seas code to input
            overseasCode = input("##############################################\nPlease enter the 3 letter Overseas Airport code\n##############################################\n")

            # sets the range for the for loop to length of rows list
            ranger = len(rows) - 1

            # for i (index) in the assigned range
            for i in range(ranger):

                # if users input matches with any code in the list
                if rows[i][0] == overseasCode:

                    # print that this airport has been selected
                    print("##############################################\n",rows[i][1],"has been selected")

                    # break subroutine and return the variables when they get called on
                    return ukCode, overseasCode
                
            # if no code is found then reports an error
            print("##############################################\nInvalid Airport Code\nPlease enter a valid Overseas code")

            del overseasCode
            
        # else
        else:

            # prints  error if inputed ukcode is invalid
            print("##############################################\nInvalid Airport Code\nPlease enter from the codes 'BOH' or 'LPL'")

            del ukCode
            
            # re-runs options subroutine
            options()

    global planeType
    global standardClass
    global firstClass
    
    # defines the flightDetails subroutine
    def flightDetails():
        planeType = None
        standardClass = None
        firstclass = None
        # sets plane type to the integer input of the user
        planeType = int(input("##############################################\nPlease enter the plane type\n1. Medium narrow body\n2. Large narrow body\n3. Medium wide body\n##############################################\n"))

        # takes away 1 from the value of plane type so it matches with the list
        planeType -= 1

        # if the planetype is the same as 0,1 or 2
        if planeType == 0 or planeType == 1 or planeType == 2:

            # prints plane info
            print("##############################################\n",
            "The plane",planes[planeType][0]," has been seleted\n",
            "Running cost per seat per 100 km is ",planes[planeType][1],"\n",
            "Maximum flight range (km) is ",planes[planeType][2],"\n",
            "Capacity if allseats are standard-class is ",planes[planeType][3],"\n",
            "Minimum number of first-class seats (if there are any) is ",planes[planeType][4],
            "\n##############################################")

            # sets the amount of first class seats to the users input
            firstClass = int(input("How many first class seats are there?\n##############################################\n"))

            # if this input is greater than 0
            if firstClass > 0:

                # if number of firstclass seats is less than the amount required for the plane
                if firstClass < int(planes[planeType][4]):
                    
                    # prints an appropriate error message (too little seats)
                    print("Your number of first class seats is lower than the minumun needed for the plane:",planes[planeType][4],"\n Please select a different aircraft or increase your amount")
                    
                    # breaks subroutine
                    return

                # else if the firstclass seats are greater than Capacity if all seats are standard-class / 2
                elif firstClass > (int(planes[planeType][3])/2):

                    # prints an appropriate error message (you have too many seats for this aircrafft)
                    print("Your number of first class seats is higher than the maximum for the plane\n Please select a different aircraft or lower your amount")

                    # breaks subroutine
                    return

                # sets the amount of standard class seats if the number of first class is appropriate to Capacity if all seats are standard-class – Number of first-class seats x 2
                standardClass = int(planes[planeType][3]) - (firstClass * 2)

                # prints the standard class size
                print("##############################################\nYour standard class size is:",standardClass)

                # breaks subroutine
                return planeType, standardClass, firstClass

            # else
            else:

                # prints appropriate error message to uer (and suggests the required amount)
                print("Your number of first class seats is lower than the minumun needed for the plane:",planes[planeType][4],"\n Please select a different aircraft or increase your amount")

                del firstClass

                # breaks subroutine
                return

        # else
        else:

            # prints appropriate error message if aircraft cannot be loaded
            print("##############################################\nUnable to load aircraft\nPlease enter a valid integer 1 - 3")

            del planeType
            
            # re-runs options subroutine
            options()

    # clears the cost per seat variable
    costPerSeat = None
    
    # main menu
    choice = input("##############################################\nPlease select your option from the list below:\n1. Enter airport details\n2. Enter flight details\n3. Enter price plan and calculate profit\n4. Clear data\n5. Quit\n##############################################\n")

    # if user selects option 1
    if choice == "1":
        
        # activates airport details subroutine
        ukCode, overseasCode = airportDetails()
        
        # activates options subroutine
        options()

    # if user selects option 2
    elif choice == "2":

        # activates flight details subroutine
        planeType, standardClass, firstClass = flightDetails()

        # activates options subroutine
        options()

    # if user selects option 3
    elif choice == "3":

        # if ukCode has a value and overseas code has a value then
        if bool(ukCode) and bool(overseasCode) == True:

            # if plane type has an assigned value then
            if bool(planeType) == True:

                # if first class has an assigned value
                if bool(firstClass) == True:

                    # if ukCode equals BOH then
                    if ukCode == "BOH":

                        # sets the plane index to 3
                        planeIndex = 3

                    # else
                    else:

                        # sets the plane index to 2
                        planeIndex = 2

                    # sets ranger to the length of the rows list - 1 (to convert from human usable to computer indexable)
                    ranger = len(rows) - 1

                    # for index in the range of ranger variable
                    for i in range(ranger):

                        # if the index of [0] on the rows list equals overseas code then
                        if rows[i][0] == overseasCode:

                            # sets the planeIndex2 to index
                            planeIndex2 = i

                    # if planes list indexed by planetype to 2 is greater than or equal to rows list indexed to planeindex2 and planeindex
                    if planes[planeType][2] >= rows[planeIndex2][planeIndex]:

                        # gather the standard and first class seat prices
                        priceStandard = input("##############################################\nPlease enter your price for standard class seats: \n##############################################\n")
                        priceFirst = input("##############################################\nPlease enter your price for first class seats: \n##############################################\n")

                        # calculates the running cost per 100km (using given formula)
                        RCper100km = planes[planeType][1].replace("£","")

                        # calculates cost per seat (using given formuala)
                        costPerSeat = float(RCper100km) * float(rows[planeIndex2][2]) / 100

                        # calculates total cost (using given formulae)
                        cost = float(costPerSeat) * (float(firstClass) + float(standardClass))

                        # calculates flight income (using given formulae)
                        flightIncome = float(firstClass) * float(priceFirst) + float(standardClass) * float(priceStandard)

                        # calculates flight profit (using given formulae)
                        flightProfit = float(flightIncome) - float(cost)

                        # Outputs calacuations to the user
                        print("##############################################")
                        print("Cost per Seat: £",costPerSeat)
                        print("Total cost is: £", cost)
                        print("Flight Income is: £", flightIncome)
                        print("Flight profit is: £", round(flightProfit, 2))

                        # returns user to main menu
                        options()

                        # breaks loop
                        return

                    # prints appropriate error message
                    else:
                        print("##############################################\nDistance of flightpath is too great for selected aircraft")

                # prints appropriate error message        
                else:
                    print("##############################################\nNumber of first class seats is invalid please enter a vaild number")
                    return
                
            # prints appropriate error message
            else:
                print("##############################################\nPlane type is invalid please enter a valid plane")
                return

        # prints appropriate error message
        else:
            print("##############################################\nUK or Overseas Code is invalid please re-check your entered code")
            return

        # returns user to main menu
        options()
        
    # if user selects option 4
    elif choice == "4":
        check = input("Are you sure? \n##############################################\n")
        print(check)
        if check.lower() == "yes":
            del ukCode
            del overseasCode
            del planeType
            del firstClass
            print("##############################################\nDeleted")

            options()
            
        else:
            print("##############################################\nData erasure aborted please choose this option again and enter 'yes' if you wish to erase your data")

            options()

    # if user selects option 5
    elif choice == "5":
        print("##############################################\nThanks for using the airport calculator!\n##############################################\n")
        exit()
        
    # else
    else:

        # if user selection is out of range prints appropriate error message 
        print("##############################################\nUnable to load page\nPlease enter a valid integer 1 - 5")

        # re-reuns subroutine
        options()

# runs options on program start

options()
