#Indra Ratna
#CS-UY 1114
#26 Oct 2018
#Lab 8
#Problem 2

def make_alpha_string(ch,n):
    ch.lower()
    start = ord(ch)
    acc = ""
    i=0
    while i <= n-1:
        if(start<=122 and start>=97):
            acc += chr(start)
        elif(start>122):
            start = 97
            acc+=chr(start)
        start+=1
        i+=1
    return acc

def test():
    result1 = make_alpha_string("y",5)
    print(result1)
    result2 = make_alpha_string("a",3)
    print(result2)

test()
