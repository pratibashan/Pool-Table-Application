

from pooltable import PoolTable,PoolTableManager

pooltablemanager =PoolTableManager()
pooltablemanager.add_table(12)


to_continue = True
while(to_continue):
    print("r - Check-in\nv - View table \nc- Check-out \nq - Quit")
    user_choice = input("Enter r/v/c/q : ")
    
    if user_choice.lower() == "v":
        pooltablemanager.view_table()

    elif user_choice.lower() == "r":

        user_table_number = int(input("Enter a Pool Table Number to Check-in(1-12): "))
        if user_table_number <=  0 or user_table_number > 12 :
            print("Pool table number not available")
        else: 
            pooltablemanager.reserve_table(user_table_number)

    elif user_choice.lower() == "c":

        user_table_number = int(input("Enter a Pool Table Number to Check-out: "))
        if user_table_number < 0 or user_table_number > 12:
            print("Pool table number not available")
        else:    
            pooltablemanager.close_table(user_table_number)
            
    elif user_choice.lower() == "q":
        to_continue = False

    else:
        print("Press a valid entry")

        







    
    