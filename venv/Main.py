from ImportCVS import package_List
import Distance

class Main:

    print("WGUPS Package Delivery System")

    start = input ("Type Exit to quit or 1 to load read file: ")



    while start != 'exit':


        if start == '1':

            print(package_List.get(1))
            print(package_List.get(1)[2])

            package_List.update(1,7,8)

            print(package_List.get(1))


            exit()


        if start == '3':

            print(package_List.get(0))
            print(package_List.get(1))
            print(package_List.get(2))
            print(package_List.get(3))
            print(package_List.get(4))
            exit()

        elif start == 'exit':
            exit()


