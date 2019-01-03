#Indra Ratna
#CS-UY 1114
#26 Oct 2018
#Lab 8
#Problem 3

def is_leap_year(year):
    if(year%4==0 and year%100!=0):
        return True
    elif(year%400==0):
        return True
    else:
        return False
def test():
    result1=is_leap_year(2016)
    print(result1)
    result2=is_leap_year(2018)
    print(result2)
test()
