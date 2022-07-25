# ![airports](https://user-images.githubusercontent.com/67003539/180818293-403e6051-be18-4053-b7c1-2f133891eccb.png)

# Flight Planning

A new airline wants to start running commercial passenger flights. In order to assess the feasibility of
proposed flights they want a program that can help them calculate the likely profitability of running a
flight between a UK airport and an overseas airport. The UK airport will be either Liverpool John
Lennon or Bournemouth International.

A comma separated (csv) file called **Airports.txt** has been provided that contains the name and code
for each overseas airport, the distance from Liverpool John Lennon airport and the distance from
Bournemouth International airport. The contents of this comma separated file are shown in **Figure 1**.

# Figure 1

| Overseas airport code | Overseas airport name        | Distance from Liverpool John Lennon (km) | Distance from Bournemouth International (km) |
| --------------------- | ---------------------------- | ---------------------------------------- | -------------------------------------------- |
| JFK                   | John F Kennedy International | 5326                                     | 5486                                         |
| ORY                   | Paris-Orly                   | 629                                      | 379                                          |
| MAD                   | Adolfo Suarez Madrid-Barajas | 1428                                     | 1151                                         |
| AMS                   | Amsterdam Schiphol           | 526                                      | 489                                          |
| CAI                   | Cario International          | 3779                                     | 3584                                         |

When the program is used, the following details will need to be entered:

1. UK airport

2. overseas airport

3. type of aircraft

4. number of first-class seats

5. price of a first-class seat

6. price of a standard-class seat.

The airline owns three types of aircraft. **Figure 2** shows the characteristics of each type of aircraft.

# Figure 2

| Type               | Running cost per seat per 100 km | Maximum flight range (km) | Capacity of all seats are standard-class | Minimum number of first-class seats |
| ------------------ | -------------------------------- | ------------------------- | ---------------------------------------- | ----------------------------------- |
| Medium narrow body | £8                               | 2650                      | 180                                      | 8                                   |
| Large narrow body  | £7                               | 5600                      | 220                                      | 10                                  |
| Medium wide body   | £5                               | 4050                      | 406                                      | 14                                  |

From the details provided by the user, the program will calculate the potential profit or loss of running
the proposed flight assuming it is at maximum capacity. Figure 3 shows how the profit or loss is
calculated. Each first-class seat takes up space for two standard-class seats.

# Figure 3

| Calculation Outcome            | Calculation                                                                                                                 |
| ------------------------------ | --------------------------------------------------------------------------------------------------------------------------- |
| Number of standard-class seats | Capacity if all seats are standard class - Number of first-class seats x 2                                                  |
| Flight cost per seat           | running cost per seat per 100 km * distance betwen the UK aiport and the overseas airport / 100                             |
| Flight cost                    | flight cost per seat * (number of first-class seats + number of standard-class seats)                                       |
| Flight Income                  | number of first-class seats * price of a first-class seat + number of standard-class seats * price of a standard-class seat |
| Flight profit                  | flight income - flight cost                                                                                                 |

**Figure 4 shows an example.**

# Figure 4

| Data                                         | Value                        |
| -------------------------------------------- | ---------------------------- |
| UK airport                                   | Liverpool John Lennon        |
| Overseas airport                             | John F Kennedy International |
| Distance                                     | 5326 kilometres              |
| Type of aircraft                             | Large narrow body            |
| Maximum flight range                         | 5600 kilometres              | 
| Running cost per seat per 100 kilometres     | £7                           |
| Capacity if all seats are standard-class     | 220                          |
| Number of first-class seats                  | 40                           |
| Number of standard-class seats: 220 - 40 × 2 | 140                          |
| Price of a standard-class seat               | £400                         |
| Price of a first-class seat                  | £1200                        |
| Flight cost per seat: 7 × 5326/100           | £372.82                      |
| Flight cost: 372.82 × (140 + 40)             | £67 107.60                   |
| Flight income: 140 × 400 + 40 × 1200         | £56 000 + £48 000 = £104 000 |
| Flight profit: 104 000 - 67 107.6            | £36 892.40                   |

The program should work in the following way:

1. The program should read in the comma separated file Airports.txt

2. A menu should be displayed allowing the user to select from the following options:

    - Enter airport details
    - Enter flight details
    - Enter price plan and calculate profit
    - Clear data
    - Quit
  
3. If the user selects the ‘Quit’ option then a suitable message should be displayed and the program
ends.

4. If the user selects the ‘Enter airport details’ option:

    a. the user should be asked to enter the three-letter airport code for the UK airport
  
    b. if the code entered is not for Liverpool John Lennon (LPL) or Bournemouth International (BOH)
then a suitable error message should be displayed and the user returned to the main menu

    c. the user should then be asked to enter the three-letter airport code for the overseas airport
  
    d. the program should check that the code for the overseas airport is valid based on the data read
from the csv file
    • if the code for the overseas airport is valid then the full name of the overseas airport should be
displayed
    • if the code for the overseas airport is not valid then a suitable error message should be
displayed

    e. the user should be returned to the main menu.
  
5. If the user selects the ‘Enter flight details’ option:

    a. the user should be asked to enter the type of aircraft to be used. The allowed types are shown
in Figure 2

    b. if the type of aircraft is not valid then a suitable error message should be displayed and the user
returned to the main menu

    c. the data in Figure 2 for that type of aircraft should then be displayed
  
    d. the user should then be asked to enter the number of first-class seats on the aircraft
  
    e. if the number of first-class seats entered is not 0 then:
    
    - if the number of first-class seats is less than the ‘minimum number of first-class seats’ then a
suitable error message should be displayed and the user returned to the main menu
    - if the number of first-class seats is greater than half the ‘capacity if all seats are standardclass’ then a suitable error message should be displayed and the user returned to the main
menu.

    f. the program should then calculate the number of standard-class seats on the aircraft using the
formula:
‘Capacity if all seats are standard-class – Number of first-class seats x 2’

    g. the user should be returned to the main menu.
    
6. If the user selects the ‘Enter price plan and calculate profit’ option:

    a. the program should check that codes for the UK and overseas airports have been entered. If not
then a suitable error message should be displayed and the user returned to the main menu

    b. the program should check if the type of aircraft has been entered. If not then a suitable error
message should be displayed and the user returned to the main menu

    c. the program should check that the number of first-class seats has been entered. If not then a
suitable error message should be displayed and the user returned to the main menu

    d. the program should check that the maximum flight range for the type of aircraft is greater than or
equal to the distance between the airports. If not then a suitable error message should be
displayed and the user returned to the main menu

    e. the user should be asked to enter the price of a standard-class seat and the price of a first-class
seat

    f. the program should then calculate the flight cost per seat, flight cost, flight income and flight
profit using the formulae shown in Figure 3

    g. the results of these calculations should be displayed and the user returned to the main menu.

7. If the user selects the ‘Clear data’ option:

    - the program should clear all data that has been entered by the user and then return the user to
the main menu.

