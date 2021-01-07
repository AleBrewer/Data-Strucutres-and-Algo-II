import csv
from HashTable import Hash_Map

with open('WGUPS Package Info.csv') as csv_file:
    reader_csv = csv.reader(csv_file, delimiter=',')

    #Calls Hashmap to create an object
    package_List = Hash_Map()

    #Creates Packages and puts them into the hash time
    #Complexity O(N)
    for row in reader_csv:
        package_ID = row[0]
        package_Address = row[1]
        package_City = row[2]
        package_State = row[3]
        package_Zip_Code = row [4]
        package_Delivery = row[5]
        package_Size = row[6]
        package_Delivery_Start = ""
        package_Delivery_End = ""
        package_AddressID = "0"
        package_Delivery_Status = "At Hub"

        iterate_Package = [package_ID,
                           package_Address,
                           package_City,
                           package_State,
                           package_Zip_Code,
                           package_Delivery,
                           package_Size,
                           package_Delivery_Start,
                           package_Delivery_End,
                           package_AddressID,
                           package_Delivery_Status]


        key = int(package_ID)
        package = iterate_Package

        package_List.add(key, package)

with open('WGUPS Location Names.csv') as csv_file:
    reader_csv = csv.reader(csv_file, delimiter=',')

    #Creates empty list for Locations
    location_List =[]

    #Creates a list from the data table
    for row in reader_csv:
        location = row[0]
        location_List.append(location)


    i = 0
    #Assigns each packages in the Hash Table with a Location ID
    #Complexity of O(N^2)
    for package in package_List.table:

        Location_Name = package_List.get(i)[1]

        #If the end of the list is found, exit loop
        if package_List.get(i)[1] == "":
            break

        #Loop checks current item in Package List and assigns it an ID when location is found
        j = 0
        for row in location_List:
            if Location_Name == location_List[j]:
                package_List.update(i,9,j)
            j = j + 1
        i = i + 1






