import csv
import datetime
import time
from ImportCVS import package_List

with open('WGUPS Distance Table.csv') as csv_file:
    reader_csv = csv.reader(csv_file, delimiter=',')

    # Create Empty List of Distances
    distance_List = []

    #Create a 2D array for Location Distances
    for row in reader_csv:

        row0 = row[0]
        row1 = row[1]
        row2 = row[2]
        row3 = row[3]
        row4 = row[4]
        row5 = row[5]
        row6 = row[6]
        row7 = row[7]
        row8 = row[8]
        row9 = row[9]
        row10 = row[10]
        row11 = row[11]
        row12 = row[12]
        row13 = row[13]
        row14 = row[14]
        row15 = row[15]
        row16 = row[16]
        row17 = row[17]
        row18 = row[18]
        row19 = row[19]
        row20 = row[20]
        row21 = row[21]
        row22 = row[22]
        row23 = row[23]
        row24 = row[24]
        row25 = row[25]
        row26 = row[26]

        data_row = []
        data_row.append(row0)
        data_row.append(row1)
        data_row.append(row2)
        data_row.append(row3)
        data_row.append(row4)
        data_row.append(row5)
        data_row.append(row6)
        data_row.append(row7)
        data_row.append(row8)
        data_row.append(row9)
        data_row.append(row10)
        data_row.append(row11)
        data_row.append(row12)
        data_row.append(row13)
        data_row.append(row14)
        data_row.append(row15)
        data_row.append(row16)
        data_row.append(row17)
        data_row.append(row18)
        data_row.append(row19)
        data_row.append(row20)
        data_row.append(row21)
        data_row.append(row22)
        data_row.append(row23)
        data_row.append(row24)
        data_row.append(row25)
        data_row.append(row26)

        distance_List.append(data_row)


# Main Algorithm used to optimized package lists
# O(N^2)
def optimize_List(truck_Package_List):

    current_LocationID = 0
    truck_List_Length = truck_Package_List.__len__()
    optimize_Package_List = []

    for length in range(0, truck_List_Length):

        shortest_Distance = 20.00
        shortest_DistanceID = 0
        iteration = 0

        for item in truck_Package_List:

            item_Address_ID = package_List.get(item - 1)[9]
            distance = distance_List[current_LocationID][item_Address_ID]

            if(float(distance) < float(shortest_Distance)):
                shortest_Distance = distance
                shortest_DistanceID = item
                shortest_Distance_Index = iteration

            iteration = iteration + 1

        current_LocationID = package_List.get(shortest_DistanceID - 1)[9]
        truck_Package_List.pop(shortest_Distance_Index)
        optimize_Package_List.append(shortest_DistanceID)

    return optimize_Package_List

# Function takes in a list, delivers the packages and returns the distance traveled
# Complexity O(N)
def deliver_Packages(truck_Package_List, truck_departure_time, end_time):

    distance_and_Time = []
    distance_Traveled = 0.0
    current_LocationID = 0

    #Truck has left, set all items to "en route"
    for item in truck_Package_List:
        package_List.update(item - 1, 10, "en route")
        package_List.update(item - 1, 7, truck_departure_time)

    truck_Time = datetime.datetime.strptime(truck_departure_time, '%H:%M:%S')
    check_end = datetime.datetime.strptime(end_time, '%H:%M:%S')


    for item in truck_Package_List:
        #Get item addressID
        item_Address_ID = package_List.get(item - 1)[9]

        #Get distacne from current location to next item in the list and add the distance to distance traveled
        distance = distance_List[current_LocationID][item_Address_ID]
        distance_Traveled = distance_Traveled + float(distance)

        #Update the current location to new location and update that the package was delivered
        current_LocationID = package_List.get(item - 1)[9]
        package_List.update(item - 1, 10, "Delivered")
        truck_Time = (truck_Time + datetime.timedelta(hours=(float(distance) / 18)))

        #Used to stop deliveries and check packages at a user given time
        if(truck_Time > check_end):
            break

        #Update Delivery time for each item
        package_List.update(item - 1, 8, truck_Time.strftime('%H:%M:%S'))


    #Get the distance and time from the last location back to the HUB and add it to truck distance and time
    distance_Traveled = distance_Traveled + float(distance_List[current_LocationID][0])
    #truck_Time = (truck_Time + datetime.timedelta(hours=(float(distance) / 18)))

    #Add final values to list and return the list
    distance_and_Time.append(distance_Traveled)
    distance_and_Time.append(truck_Time)

    return distance_and_Time













