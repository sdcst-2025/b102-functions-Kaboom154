"""
### Assignment 1
#### Random Recipe
Create a function that chooses a random ingredient from a list and returns a string that contains ingredient along with a random value

Your program should call the function several times and display the result.

Criteria:
* use a loop to repeat a block of commands 5 times
* each block should retrieve one value from the function and display it on a line
* you will need to make use of the "random" module (import random) to access the class methods/functions to help you generate random numbers and select random items from a list.

Sample Output:
Your recipe:
134 cup of sugar
88 cup of milk
91 cup of chicken
145 cup of butter
15 cup of salt
"""
import random

def randomIngredient():
    ingredientList=(random.sample(['sugar','milk','chicken','butter','salt'],k=5))
    return ingredientList

z=randomIngredient()

def randomNumber():
    randNumb=random.randint(1,100)
    return randNumb

print('funky chicken recipe:')
for i in range(0,5):
    x=z.pop(0)
    # function randomIngredient() runs anew every time it is called; find way to make it stay same
        #(function randomIngredient() has been defined as a variable to avoid rerunning as a function)
    print(randomNumber(),'cup(s) of',x)
