#Author: Alexander Brewer
#Student ID: 001203903


from ImportCVS import package_List
from DeliveryTrucks import deliveryTrucks
from SerachPackages import search_Options
import datetime
import time

class Main:

    print("")
    print("")
    print("--------------WGUPS Package Delivery System--------------")

    #Options of the main menu
    def main_Menu():
        print("")
        print("Main Menu:")
        print("1 = Deliver all packages")
        print("2 = Check status of packages at a specified time")
        print("3 = Options to search for packages")
        print("exit = To close program")
        print("")

        start = input ("Command: ")

        return start

    start = main_Menu()

    while start != 'exit':

        # Deliver Packages and return time total time and distance
        if start == '1':
            deliveryTrucks(start, '')
            start = main_Menu()

        elif start == '2':
            print("")
            print("Type time as HH:MM:SS")
            time_Check = input("Check packages at time: ")
            deliveryTrucks(start, time_Check)
            start = main_Menu()

        #Search Package Options
        elif start == '3':
            search_Options()
            start = main_Menu()

        else:
            print("Command not Recognized")
            print("")
            start = input("Command: ")

    exit()