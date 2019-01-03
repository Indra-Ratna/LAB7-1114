#Indra Ratna
#CS-UY 1114
#26 Oct 2018
#Lab 8
#Problem 4

def print_n_ints(start,n):
    acc=""
    for i in range (start,start+n):
        acc+=(str(i)+"\n")
    print(acc)

def test():
    print_n_ints(5,6)
    print_n_ints(-3,5)

test()
