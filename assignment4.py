"""
### Assignment 4
#### Prime factorization
Create a program that incorporates assignment 2 and 3 to do the prime factorizations for a number.  You will need to develop an algorithm to determine how you can do this.  If you can't figure it out by the beginning of next class, your teacher will provide you with some pseudocode/a method for determining how you can do this.
"""
'''
example:
100 %2 = 0
new number is 100/2 = 50.
add 2 to the list of prime factors and now check 50
50 % 2 = 0
new number is 50/2 = 25
add 2 to the list of prime factors, and now check 25
25% 2 = 1
move on to next number
'''

def get_integer_input():
    integer=input('integer:')
    return int(integer)

integerInput = get_integer_input()
integerList=[]

def divCheck():
    #while divCheck() > 0:
    #for i in range (0,10):
        if integerInput % 2 == 0:
            integerList.append(2)
            return integerInput / 2
        if integerInput % 5 == 0:
            integerList.append(5)
            return integerInput / 5
        if integerInput % 7 == 0:
            integerList.append(7)
            return integerInput / 7
        
print(integerInput,integerList,divCheck())
