#Indra Ratna
#CS-UY 1114
#26 Oct 2018
#Lab 8
#Problem 5

def print_shifted_triangle(lines,offset,symbol):
    line1 = lines
    num_space = ((2*lines)-1)//2
    num_symbol = 1
    while(line1>0):
       print(" "*offset,end="") 
       print(" "*num_space+symbol*num_symbol+" "*num_space)
       num_symbol+=2
       num_space-=1
       line1-=1
def print_pine_tree(num_triangles,symbol):
    lines = 2
    space = num_triangles-1
    final_lines = num_triangles+2
    while(lines<final_lines):
        print_shifted_triangle(lines,space,symbol)
        lines+=1
        space-=1
        
def test():
    print_shifted_triangle(3,0,"+")
    print_shifted_triangle(4,5,"#")
    print_pine_tree(3,"#")
test()
