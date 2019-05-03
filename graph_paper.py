"""
This program prints graph paper to user specifications.
"""


import sys

rows_boxes = int(input("How many rows of boxes? "))
columns_boxes = int(input("How many columns of boxes? "))
rows_spaces = int(input("How many rows of spaces in each box? "))
columns_spaces = int(input("How many columns of spaces in each box? "))



for i in range(rows_boxes):

    print(columns_boxes*("+" + columns_spaces*"-"), end = "")

    print('+')

    for h in range(rows_spaces):
        print(columns_boxes*("|" + columns_spaces*" "), end = "")
        print('|')
       
print(columns_boxes*("+" + columns_spaces*"-") + '+', end = "")


sys.exit(0)
