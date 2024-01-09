
# ''' for multiline 
print('''
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
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
** What would you like to order? **
***********************************''')
# ChatGPT assisted
# comments are for my notes

# {} = Dictionary
userOrder = {}

while True:
    userInput = input('> ')
    
    #  break exits while loop
    if userInput.lower() == 'quit':
        break
    
    if userInput in userOrder:
        userOrder[userInput] += 1
    else:
        userOrder[userInput] = 1
    
    orderAmount = userOrder[userInput]
    # f for concatenation 
    print(f"** {orderAmount} {'orders' if orderAmount > 1 else 'order'} of {userInput} {'have' if orderAmount > 1 else 'has'} been added to your meal **")

print("GoodBye!")

