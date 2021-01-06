import csv
from HashTable import Hash_Map

with open('WGUPS Package Info.csv') as csv_file:
    reader_csv = csv.reader(csv_file, delimiter=',')

    #Calls Hashmap to create an object
    insert_package = Hash_Map()

    #Create Truck lists with their packages
    truck_One = [1,4,6,12,17,21,25,28,31,32,40]
    truck_Two = [2,3,5,7,8,9,10,18,27,29,30,33,35,36,37,38]
    truck_Three = [11,13,14,15,16,19,20,22,23,24,26,34,39]

    #Creates Packages and puts them into the hash time
    #Complexity O(N)
    for row in reader_csv:
        package_ID = row[0]
        package_Address = row[1]
        package_City = row[2]
        package_State = row[3]
        package_Zip_Code = row [4]
        package_Size = row[5]
        package_delivery = row[6]
        package_Delivery_Start = ""
        package_AddressID = "0"
        package_Delivery_Status = "At Hub"

        iterate_Package = [package_ID,
                           package_Address,
                           package_City,
                           package_State,
                           package_Zip_Code,
                           package_Size,
                           package_delivery,
                           package_Delivery_Start,
                           package_AddressID,
                           package_Delivery_Status]


        key = int(package_ID)
        package = iterate_Package

        insert_package.add(key, package)

with open('WGUPS Location Names.csv') as csv_file:
    reader_csv = csv.reader(csv_file, delimiter=',')

    location_List =[]

    for row in reader_csv:
        location = row[0]
        location_List.append(location)


    i = 0
    for package in insert_package.table:

        Location_Name = insert_package.get(i)[1]

        if insert_package.get(i)[1] == "":
            break

        j = 0
        for row in location_List:
            if Location_Name == location_List[j]:
                insert_package.update(i,7,j)
            j = j + 1
        i = i + 1






