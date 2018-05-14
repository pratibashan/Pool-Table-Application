
from datetime import datetime, timedelta
from random import *
class PoolTable:

    def __init__ (self,table_number):
        self.table_number = table_number
        self.status = "Not Occupied"
        self.start_date_time = None
        self.startdate_str = ""
        self.enddate_str=""
        self.end_date_time = None
        self.total_time_played = 0.0
        self.cost = 0.00

class PoolTableManager:

    def __init__(self):
        self.pooltables = []
    

    def add_table(self,tablecount):

        for index in range(0,tablecount,1):
            self.pooltables.append(PoolTable(index + 1))

    # def start_time(self):
    #     self.status ="Occupied"
    #     self.start_date_time = datetime.now()
    #     return self.start_date_time

    # def end_time(self):
    #     self.status = "Not Occupied"
    #     self.end_date_time = datetime.now() - timedelta(minutes = 30) 
    #     return self.end_date_time


    def view_table(self):
        print("*"* 100)
        print("\t\t\t\tView Table")
        print("*"*100)
        print(f"   Table Number\t\t   Status\t\t      StartDate\t\t Total Time Played")
        for tb in self.pooltables:    
            if tb.status == "Occupied":
                
                print(f"\t{tb.table_number}\t\t  {tb.status}\t\t{tb.startdate_str}\t\t{tb.total_time_played}")
       
            else:
                
                print(f"\t{tb.table_number}\t\t{tb.status}")

    def reserve_table(self,user_table_num):
        print("*"* 50)
        print("Reserve Table")
        print("*"*50)
        for tb in self.pooltables:
            
            if tb.table_number == user_table_num:
                 
                if tb.status == "Not Occupied":
                    tb.status ="Occupied"
                    rand_num = randint(50,500)
                    tb.start_date_time = datetime.now()- timedelta(minutes = rand_num)
                    tb.startdate_str = tb.start_date_time.strftime("%Y-%m-%d %H:%M:%S")
                    print("You are checked in to")
                    print(f"Pool Table\t:   {tb.table_number}\nStatus          : {tb.status}\n\
Start Date Time : {tb.startdate_str}")

                else:
                    print(f"Pool Table {tb.table_number} is currently occupied.")
                break
        print("*" * 50)

    def close_table(self,tablenumber):
        print("*"* 50)
        print("Check Out")
        print("*"*50)
        mins = 0
        hours = 0
        for tb in self.pooltables:
            if tb.table_number == tablenumber:
                if tb.status == "Occupied":
                    tb.status = "Not Occupied"
                    tb.end_date_time =datetime.now()
                    tb.enddate_str = tb.end_date_time.strftime("%Y-%m-%d %H:%M:%S")
                    
                    totaltime = tb.end_date_time - tb.start_date_time      
                    totaltime_mins = totaltime.seconds/60
                    
                    if totaltime_mins > 60:
                        hours =int(totaltime_mins/60)
                        mins = int(totaltime_mins % 60)
                        tb.total_time_played = "{}hour {:02d}mins".format(hours,mins)
                    else:
                        tb.total_time_played = totaltime_mins
                   
                    if mins > 0:
                        hours += 1
                        tb.cost = 30 * hours
                       
                    print("You are checked out from")
                    print(f"Pool Table \t  :  {tb.table_number}\nStart Date Time\t  : {tb.startdate_str}\n\
End Date Time \t  : {tb.enddate_str}\nTotal Time Played : {tb.total_time_played}\nCost\t\t  : \
${tb.cost}")

                    today = datetime.today()
                    filename = today.strftime( '%m-%d-%Y')+ ".txt" 
                
                    with open(filename,'a') as file:
                        file.write("\n \n")
                        file.write("Pool Table Number\t :  "+ str(tb.table_number))                       
                        file.write("\nStart Date TIme\t\t :  "+ str(tb.start_date_time))                        
                        file.write("\nEnd Date Time\t\t :  " + str(tb.end_date_time))                        
                        file.write("\nTotal Tmie Played\t :  "+str(tb.total_time_played))
                        file.write("\nTotal Cost\t\t\t :  "+"$"+str(tb.cost))                             
                else: 
                    print("Pool Table is not occupied.")
                break

        print("*"*50)  
        

    
    