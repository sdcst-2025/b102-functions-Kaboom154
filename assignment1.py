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
    ingredientList=random.sample(['sugar', random.randint(1,100),'milk','chicken','butter','salt'],k=5)
    #randomNumber=random.randint(0,100)
    return ingredientList
    #,randomNumber



print(randomIngredient())

for i in range(0,5):
    #x=ingredientlist.pop(0)
    x=randomIngredient().pop(0)
    # function here runs anew every time it is called; find way to make it stay same
    print(x)
