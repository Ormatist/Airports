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
