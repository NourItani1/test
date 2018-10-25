#Name: Nour Itani
#AubNET: nni05
#ID: 201800561

import sys
n= int(sys.argv[1]) #number of sides
l= int(sys.argv[2]) #length of sides

import turtle 

def cpolygon(n, l):
    for i in range (n):
        if i %2== 0:
            turtle.color("black")
        else:
            turtle.color("red")
        turtle.forward(l)
        turtle.left(360/n)

cpolygon(n, l)
turtle.done()