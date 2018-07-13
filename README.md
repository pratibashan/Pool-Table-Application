# Pool Table Management Application

### Overview:
I created this Application using PYTHON.
This Application allows us to view all the  pool tables, along with check-ins and check-outs .The pool tables can be checked in only if the table is not Occupied .Once the the table is checked out, a log is written in the text file to keep track of all the tables.


---

```python
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
```