# Program to find the number of bits needed to be swapped to make two numbers equal
def totalflips(n1,n2):
    # Variable to count flips required 
    flips=0
    # Get the last bit of both the numbers and check if both of them are same. If yes, no flip required, else, flip is required
    while(n1>0 or n2>0):
        t1=(n1&1)
        t2=(n2&1)
        if(t1!=t2):
            flips+=1
        # Right shift both the numbers
        n1>>=1
        n2>>=1
    return flips
n1=int(input("Enter the first number"))
n2=int(input("Enter the second number"))
print("\nNumber of flips needed:",totalflips(n1,n2))