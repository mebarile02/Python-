"""
This is a function that takes in a natural number n.  It assumes the user will
enter an integer, but not necessarily a natural number.

"""

def explode_seq(n):
    
    cond = True
    
    while cond:
        if n > 0:
            cond = False
        else:
            n = int(input('Enter an integer greater than 0: '))

    if n == 1:
        return 1
    elif n == 2:
        return 2
    else: return explode_seq(n-1)+explode_seq(n-2)



