import sys
n= int(sys.argv[1]) #rows
c= str(sys.argv[2]) #symbol

def diamond_top(n, c):
    for l in range (0, n):
        for space in range (1,n-l+1):
            print(" ", end= "")
        print("/", end= "")
        for symbol in range (1,(2*l)+1):
            print(c, end= "")
        print("\\")
        for space in range (1,n-l+1):
            print("", end= "")
        

def diamond_bottom(n, c):
    for l in range (n-1, -1, -1):
        for space in range (1,n-l+1):
            print(" ", end= "")
        print("\\", end= "")
        for symbol in range (1,(2*l)+1):
            print(c, end= "")
        print("/")
        for space in range (1,n-l+1):
            print("", end= "")
            
     
        
        

diamond_top(n, c)
diamond_bottom(n, c)