
welcome = """ 
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **"""
print(welcome)

menu = """
Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears"""

print(menu)

prompt = """
***********************************
** What would you like to order? **
***********************************
"""



while True:
    order = input(prompt)
    if order =="quit":
        break

    item_count=1
    
    print(f"You {item_count} ordered something")

print("Thanks for coming")


# do stuff



