'''
Meal Planner
v0.1
By Advait Redkar
'''
#-------Imports---------

from random import choice

#-------- A. Functions-------------

# A1. Choose dishes

def chooseDishes(days):
    while len(myMenu) < int(days):
        chosenDish = choice(foodWeLike)
        if chosenDish not in myMenu:
            myMenu.append(chosenDish)
    print("Done! Here is your menu...")
    print()
    for dish in myMenu:
        print(dish)
    print()
    print("Out of all these dishes, my favorite has to be..." + choice(myMenu))

    
    '''
    1. Choose random dish from foodWeLike - Done
    2. Check dish hasn't been chosen. If not, add to myMenu - Done
    3. Repeat until we have required number of dishes in myMenu- Done
    '''
    

# A2. Build shopping list function

def buildShoppingList():
    myShoppingList= []
    if "Butter Chicken" in myMenu:
        myShoppingList.append(BtrChx)
    if "Salmon" in myMenu:
        myShoppingList.append(Salmon)
    if "Creamy Tomato Pasta" in myMenu:
        myShoppingList.append(CTP)
    if "Tacos" in myMenu:
        myShoppingList.append(Tacos)
    if "Shrimp Fried Rice" in myMenu:
        myShoppingList.append(SFR)
    if "Veggie Chili" in myMenu:
        myShoppingList.append(VC)
    if "Chili Chicken" in myMenu:
        myShoppingList.append(CC)
    print()    
    for dish in myShoppingList:
        for ingredient in dish:
            print(ingredient)
    print()
    print("Wahoo!! Eat Up!")
        
#--------- B. Lists----------------

foodWeLike = ["Butter Chicken" , "Salmon" , "Creamy Tomato Pasta", "Tacos", "Shrimp Fried Rice", "Veggie Chili", "Chili Chicken"]


BtrChx = ["Tomato Sauce", "Heavy Cream", "Butter", "Chicken"]
Salmon = ["Salmon", "Goat Cheese", "Olive Oil"]
CTP = ["Pasta Sauce", "Pasta", "Heavy Cream"]
Tacos = ["Tortillas", "Salsa", "Chicken Tenders"]
SFR = ["Shrimp", "Rice (Cooked)", "Carrots", "Sesame Oil", "Oyster Sauce"]
VC = ["Beyond meat veggie crumble", "Beans", "Crushed Tomatoes"]
CC = ["Green Chilis", "Minced Garlic", "Soy Sauce", "Chicken"]

myMenu = []

#1. How many days to plan?

print("Hello, I'm Munch! I'll help you to plan your dinner menu...")

answer = input("How many days would you like me to plan? ")

print("OK, I'm going to plan " + answer + " dinner(s) from your favourite meals list")

#2. Choose Dishes

chooseDishes(answer)
print()

#3. Build a shopping list?

answer = input("Would you like a shopping list for this menu? ")

if answer == "y":
    buildShoppingList()
if answer == "n":
    print("See ya next time!!")
else:
    print("Sorry , didn't get that!")
    











    
