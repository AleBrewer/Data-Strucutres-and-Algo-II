from OptimizeDeliver import optimize_List
from OptimizeDeliver import deliver_Packages
from ImportCVS import package_List

def deliveryTrucks(option, time):
    #List and time for Truck 1
    truck_One = [1, 4, 6, 12, 17, 21, 25, 28, 29, 31, 32, 40]
    truck_One_Departure = '9:05:00'

    #List and time for Truck 2
    truck_Two = [2, 3, 5, 7, 8, 9, 10, 18, 27, 33, 35, 36, 38]
    truck_Two_Departure = '10:20:00'

    #List and time for Truck 3
    truck_Three = [11, 13, 14, 15, 16, 19, 20, 22, 23, 24, 26, 30, 34, 37, 39]
    truck_Three_Departure = '8:00:00'

    #Optimized Deliver order of each list
    truck_One_Optimzied = optimize_List(truck_One)
    truck_Two_Optimized = optimize_List(truck_Two)
    truck_Three_Optimized = optimize_List(truck_Three)

    #Option 1 Deliver all Packages
    if option == '1':

        #Initialzie final time and final Distance
        final_Time = ""
        final_Distacne = 0.0

        #Deliver packages for each truck
        distance_time_truck_One = deliver_Packages(truck_One_Optimzied, truck_One_Departure, '23:59:59')
        distance_time_truck_Two = deliver_Packages(truck_Two_Optimized, truck_Two_Departure, '23:59:59')
        distance_time_truck_Three = deliver_Packages(truck_Three_Optimized, truck_Three_Departure, '23:59:59')

        #Add each total distance for each truck
        final_Distacne = distance_time_truck_One[0] + distance_time_truck_Two[0] + distance_time_truck_Three[0]

        #Print time of last truck to leave the HUB and the final Distance
        print("Final package Delivered at: " + (distance_time_truck_Two[1]).strftime('%H:%M:%S'))
        print("Total distance traveled: " + str(final_Distacne) + " Miles")

    #Option 2 check package status at a specific time
    #Space Time O(N)
    if option == '2':
        list_Length = package_List.table.__len__()

        #Change all packaged to At Hub and Set Deliver time to blanck
        for package in range(0, list_Length):
            package_List.update(package - 1, 8, "")
            package_List.update(package - 1, 10, "At Hub")

        #Try to deliver Truck one at user given time, if user time is an invalid format
        #Returns 1 and will not try to deliver the other trucks
        distance_time_truck_Three = deliver_Packages(truck_Three_Optimized, truck_Three_Departure, time)



        if distance_time_truck_Three != 1:
            distance_time_truck_Two = deliver_Packages(truck_Two_Optimized, truck_Two_Departure, time)
            distance_time_truck_One = deliver_Packages(truck_One_Optimzied, truck_One_Departure, time)

            #Prints all packages
            final_Distacne = distance_time_truck_One[0] + distance_time_truck_Two[0] + distance_time_truck_Three[0]
            print("Total distance traveled: " + str(final_Distacne) + " Miles")

            for package in range(0, list_Length):
                print(package_List.get(package))
