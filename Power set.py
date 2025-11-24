# Program to find power set of a set
import math
def printpowerset(set,setsize):
    powersetsize=(int)(math.pow(2,setsize))# Find total elements possible in the power set
    outer=0
    inner=0
    for outer in range(0,powersetsize):
        for inner in range(0,setsize):
            # Check if inner bit in the outer is set then print the element from the set
            if ((outer & (1<<inner))>0):
                print(set[inner],end="")
        print("")
size=int(input("Enter the array size"))
set=[]
for i in range(0,size):
    n=int(input("Enter the element"))
    set.append(n)
printpowerset(set,len(set))