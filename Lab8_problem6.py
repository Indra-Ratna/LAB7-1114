#Indra Ratna
#CS-UY 1114
#26 Oct 2018
#Lab 8
#Problem 6

def print_month_calendar(num_day,start_day):
    print("Mon"+"\t"+"Tue"+"\t"+"Wed"+"\t"+"Thu"+"\t"+"Fri"+"\t"+"Sat"+"\t"+"Sun"+"\t")
    tab_val = 9-start_day
    x=0
    if(start_day>0):
        print("\t"*(start_day-1),end="")
    for i in range(1,num_day+1):
        if(i%tab_val==0):
            print("\n"+str(i)+"\t",end="")
            tab_val+=7
            x=i
        else:
            print(str(i)+"\t",end="")
    print()
    last = (num_day-x)+1
    return last
   
def return_last(num_day,start_day):
    tab_val = 9-start_day
    x=0
    acc=0
    for i in range(1,num_day+1):
        if(i%tab_val==0):
            tab_val+=7
            x=i
            
    last = (num_day-x)+1
    return last

def is_leap_year(year):
    if(year%4==0 and year%100!=0):
        return True
    elif(year%400==0):
        return True
    else:
        return False
def print_year_calendar(year,start_day):
    months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
    start = start_day
    for i in range(len(months)):
        print(months[i]+" "+str(year))
        if(i==3 or i==8 or i==5 or i==10):
            print_month_calendar(30,start)
            start = return_last(30,start)
        elif(i==1):
            if is_leap_year(year):
                print_month_calendar(28,start)
                start = return_last(28,start)
            else:
                print_month_calendar(29,start)
                start = return_last(29,start)
        else:
            print_month_calendar(31,start)
            start = return_last(31,start)
        start+=1
        if(start==8):
            start=1
        print()
def test():
    #print(return_last(31,4))
    print_month_calendar(30,6)
    print_year_calendar(2016,5)
test()
