"""
list_temp.py

This file takes in a list of degrees Farenheit from the user and returns
degrees Celcius.

"""

import sys

def conToCelc(faren):
    """
    converts farenheit to celcius
    """
    return (faren - 32)*(5/9)

list_faren = []  # empty list

while True:
    
    try:
        temp = input("Enter degrees Farenheit to convert to \
Celcius (or e to Exit): ")
    except EOFError:
        sys.exit(0)                

    if temp == 'e':
        break
    
    try:
        list_faren.append(float(temp))
    except ValueError:
        print("Not a number!")


list_faren.sort()  #put numbers into ascending order

d = "\u00b0"   #degree symbol

for temp in list_faren:
    print(f"{temp:10.2f}{d}F    ==> {conToCelc(temp):10.2f}{d}C")

sys.exit(0)
    




