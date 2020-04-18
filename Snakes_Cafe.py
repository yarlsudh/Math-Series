print("""
****************************************    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    ****

** To quit at any time, type "quit" **
**************************************

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
Unicorn Tears

***********************************
""")
item = input("** What would you like to order? **")
i =0
while(item):
    j=i+1
    print(f"** {j} order of {item} have been added to your meal **")
    item = input("Would you like to order another item?")
    i=i+1
    if(item=="quit"):
        break

