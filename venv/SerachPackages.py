from ImportCVS import package_List

#Takes in the Users input and location for the item they are searching
def search_List(search_Critrea, search_Critrea_ID):

    #Create and empty list for items found
    packages_Found = []
    package_Length = package_List.table.__len__()

    #Check Hash table for user criteria
    for package in range(0, package_Length):
        if search_Critrea == package_List.get(package)[search_Critrea_ID]:
            packages_Found.append(package_List.get(package))

    #Print all items found or print "No Packages found"
    if packages_Found.__len__() > 0:
        for package in packages_Found:
            print(package)
    else:
        print("No packages found")

#Option for the User to serach for package(s)
def search_Options():

    print("")
    print("1 = Search by Package ID Number")
    print("2 = Search by Delivery address")
    print("3 = Serach by City")
    print("4 = Serach by Zip Code")
    print("5 = Search by Delivery Deadline")
    print("6 = Search by Package Weight")
    print("7 = Serach by Delivery Status")
    print("")

    search_Option = input("Command: ")

    # Search by Package ID
    if search_Option == '1':
        package_ID = input("Package ID: ")

        # Space Time O(1)
        try:
            print("")
            print(package_List.get(int(package_ID) - 1))
        except:
            print("Package(s) not found")


    # Search by Package Address
    # Space Time O(N)
    elif search_Option == '2':
        package_Address = input("Delivery Address: ")
        search_List(package_Address, 1)

    # Search by City
    # Space Time O(N)
    elif search_Option == '3':
        package_City = input("City: ")
        search_List(package_City, 2)

    # Seach by ZipCode
    # Space Time O(N)
    elif search_Option == '4':
        package_Zip = input("Zip Code: ")
        search_List(package_Zip, 4)

    # Seach by ZipCode
    # Space Time O(N)
    elif search_Option == '5':
        print("Enter time as: HH:MM:SS")
        package_Deadline = input("Delivery Deadline: ")
        search_List(package_Deadline, 5)

    # Search by Package Weight
    # Search Time O(N)
    elif search_Option == '6':
        package_Weight = input("Package Weight: ")
        search_List(package_Weight, 6)

    # Search by by Delivery Status
    # Seach Time O(N)
    elif search_Option == '7':
        print("")
        print("1 = At Hub")
        print("2 = En route")
        print("3 = Deliverd")
        print("")

        user_Selection = input("Command: ")

        if user_Selection == '1':
            search_List("At Hub",10)

        elif user_Selection == '2':
            search_List("en route", 10)

        elif user_Selection == '3':
            search_List("Delivered", 10)

        else:
            print("Command not recognized")
