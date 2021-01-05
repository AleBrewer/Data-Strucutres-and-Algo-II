from ImportCVS import insert_package
#from HashTable import Hash_Map

class Main:

    print("WGUPS Package Delivery System")

    start = input ("Type Exit to quit or 1 to load read file: ")



    while start != 'exit':


        if start == '1':

            print(insert_package.get(1))
            print(insert_package.get(1)[2])

            insert_package.update(1,7,8)


            print(insert_package.get(1))




            exit()

        if start == '2':
            # Creates a list containing 5 lists, each of 8 items, all set to 0
            Matrix = [[0]*5 for i in range(5)]
            Matrix [0][0] = "Moo"

            print (Matrix)

            exit()

        elif start == 'exit':
            exit()


