# Small program that takes 5 integers and returns the maximum and the minimum value from a manually populated list!


numb1 = int(input("Enter 1st number as input: "))
numb2 = int(input("Enter 2nd number as input: "))
numb3 = int(input("Enter 3rd number as input: "))
numb4 = int(input("Enter 4th number as input: "))
numb5 = int(input("Enter 5th number as input: "))

table = [numb1,numb2,numb3,numb4,numb5]

print ("The maximum value you entered is:", max(table),"The minimum value you entered is:", min(table))