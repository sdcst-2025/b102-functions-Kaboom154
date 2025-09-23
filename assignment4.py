"""
### Assignment 4
#### Prime factorization
Create a program that incorporates assignment 2 and 3 to do the prime factorizations for a number.  You will need to develop an algorithm to determine how you can do this.  If you can't figure it out by the beginning of next class, your teacher will provide you with some pseudocode/a method for determining how you can do this.
"""
def get_integer_input():
    integer=input('integer:')
    return int(integer)

def divCheck():
    if get_integer_input() % 2 == 0:
        return True
        

print(divCheck())
