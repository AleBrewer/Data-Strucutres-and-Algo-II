import csv
import datetime
from ImportCVS import package_List

with open('WGUPS Distance Table.csv') as csv_file:
    reader_csv = csv.reader(csv_file, delimiter=',')

    # Create Truck lists with their packages
    truck_One = [1, 4, 6, 12, 17, 21, 25, 28, 31, 32, 40]
    truck_Two = [2, 3, 5, 7, 8, 9, 10, 18, 27, 29, 30, 33, 35, 36, 37, 38]
    truck_Three = [11, 13, 14, 15, 16, 19, 20, 22, 23, 24, 26, 34, 39]

    truck_One_Optimzed = []
    truck_Two_Optimzed = []
    truck_Three_Optimzed = []

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

    current_LocationID = 0
    truck_One_List_Length =  truck_One.__len__()

    for length in range(0, truck_One_List_Length):

        shortest_Distance = 20.00
        shortest_DistanceID = 0
        iteration = 0
        for item in truck_One:

            item_Address_ID = package_List.get(item - 1)[7]
            distance = distance_List[current_LocationID][item_Address_ID]

            if(float(distance) < float(shortest_Distance)):
                shortest_Distance = distance
                shortest_DistanceID = item
                shortest_Distance_Index = iteration

            iteration = iteration + 1

        current_LocationID = package_List.get(shortest_DistanceID - 1)[7]
        truck_One.pop(shortest_Distance_Index)
        truck_One_Optimzed.append(shortest_DistanceID)




    print(truck_One_Optimzed)