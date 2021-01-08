#Author: Alexander Brewer
#Student ID: 001203903


from ImportCVS import package_List
from Distance import optimize_List
from Distance import deliver_Packages
import Distance
import datetime
import time

class Main:

    print("")
    print("")
    print("--------------WGUPS Package Delivery System--------------")
    print("")

    print("Main Menu:")
    print("1 = Deliver all packages")
    print("2 = Check status of packages at a specified time")
    print("3 = Options to search for packages")
    print("exit = to close program")
    print("")

    start = input ("Command: ")




    while start != 'exit':


        if start == '1':

            truck_One = [1, 4, 6, 12, 17, 21, 25, 28, 29, 31, 32, 40]
            truck_One_Departure = '9:05:00'

            truck_Two = [2, 3, 5, 7, 8, 9, 10, 18, 27, 33, 35, 36, 38]
            truck_Two_Departure = '10:20:00'

            truck_Three = [11, 13, 14, 15, 16, 19, 20, 22, 23, 24, 26, 30, 34, 37, 39]
            truck_Three_Departure = '8:00:00'

            truck_One_Optimzied = optimize_List(truck_One)
            truck_Two_Optimized = optimize_List(truck_Two)
            truck_Three_Optimized = optimize_List(truck_Three)

            final_Time = ""
            final_Distacne = 0.0

            distance_time_trcuk_One = deliver_Packages(truck_One_Optimzied, truck_One_Departure, '23:59:59')
            distance_time_trcuk_Two = deliver_Packages(truck_Two_Optimized, truck_Two_Departure, '23:59:59')
            distance_time_truck_Three = deliver_Packages(truck_Three_Optimized, truck_Three_Departure, '23:59:59')

            final_Distacne = distance_time_trcuk_One[0] + distance_time_trcuk_Two[0] + distance_time_truck_Three[0]

            print("Final package Delivered at: " + (distance_time_trcuk_Two[1]).strftime('%H:%M:%S'))
            print("Total distance traveled: " + str(final_Distacne) + " Miles")



            #print("Truck Three:")
            #print(truck_Three_Optimized)
            #time_List = deliver_Packages(truck_Three_Optimized, truck_Three_Departure, '23:59:59')
            #print(time_List[0])
            #print(time_List[1].strftime('%H:%M:%S'))
            #print("")

            #print(deliver_Packages(truck_Two_Optimized))
            #print(deliver_Packages(truck_Three_Optimized))

            #for item in range(0, 40):
            #    print(package_List.get(item))

            print("")
            start = input("Command: ")


        elif start == '2':
            print(":)")

            print("")
            start = input("Command: ")


        elif start == '3':

            s = "08:10:10"

            timestamp = (datetime.datetime.strptime(s, '%H:%M:%S'))


            timestamp = (timestamp + datetime.timedelta(minutes=2.5)).strftime('%H:%M:%S')

            print(timestamp)

            print("")
            start = input("Command: ")


        elif start == 'exit':
            exit()

        else:
            print("Command not Recognized")
            print("")
            start = input("Command: ")
