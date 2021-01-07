from ImportCVS import package_List
from Distance import optimize_List
from Distance import deliver_Packages
import Distance
import datetime
import time

class Main:

    print("WGUPS Package Delivery System")

    start = input ("Type Exit to quit or 1 to load read file: ")



    while start != 'exit':


        if start == '1':

            truck_One = [1, 4, 6, 12, 17, 21, 25, 28, 31, 32, 40]
            truck_One_Departure = '9:05:00'
            truck_Two = [2, 3, 5, 7, 8, 9, 10, 18, 27, 29, 30, 33, 35, 36, 37, 38]
            truck_Three = [11, 13, 14, 15, 16, 19, 20, 22, 23, 24, 26, 34, 39]


            #print("Not optimized:")
            #print(deliver_Packages(truck_One))
            #print(deliver_Packages(truck_Two))
            #print(deliver_Packages(truck_Three))
            #print("")

            truck_One_Optimzied = optimize_List(truck_One)
            truck_Two_Optimized = optimize_List(truck_Two)
            truck_Three_Optimized = optimize_List(truck_Three)

            print(truck_One_Optimzied)

            print("Optimzed: ")
            time_List = deliver_Packages(truck_One_Optimzied, truck_One_Departure)
            print(time_List[0])
            print(time_List[1].strftime('%H:%M:%S'))


            #print(deliver_Packages(truck_Two_Optimized))
            #print(deliver_Packages(truck_Three_Optimized))

            for item in range(0, 29):
                print(package_List.get(item))

            exit()


        if start == '3':

            s = "08:10:10"

            timestamp = (datetime.datetime.strptime(s, '%H:%M:%S'))


            timestamp = (timestamp + datetime.timedelta(minutes=2.5)).strftime('%H:%M:%S')

            print(timestamp)



            exit()


        elif start == 'exit':
            exit()


