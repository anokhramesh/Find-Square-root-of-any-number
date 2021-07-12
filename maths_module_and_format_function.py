print ("A program to find the Square root of a number")
print("---------------------------------------------")
import math
while True:
    num = int(input("Enter a number to Find Square root.\n"))
    sq_of_num = math.sqrt(num)
    format_sq_of_num = format(sq_of_num,".3f")
    print("Square root of",num,"is =",format_sq_of_num)
    print("-------------------------------------------")
