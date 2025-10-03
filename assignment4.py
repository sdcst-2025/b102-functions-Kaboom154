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
for a in range (2,integerInput-1):
    for n in range (2,a):  #factors of integer
            if integerInput % n == 0:
                integerList.append (n)
                integerInput = integerInput / n




print(integerList)

