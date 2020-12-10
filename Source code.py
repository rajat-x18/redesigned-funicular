
from IPython.display import clear_output
cart = [ ]
def addItem(item):
clear_output( )
cart.append(item)
print( "{ } has been added.".format(item) )
def removeItem(item):
clear_output( )
try:
cart.remove(item)
print( "{ } has been removed.".format(item) )
except:
print("Sorry we could not remove that item.")
def showCart( ):
clear_output( )
if cart:
print("Here is your cart:")
for item in cart:
print( "- { }".format(item) )
else:
print("Your cart is empty.")
def clearCart( ):
clear_output( )
cart.clear( )
print("Your cart is empty.")
def main( ):
done = False
while not done:
ans = input("quit/add/remove/show/clear: ").lower( )
if ans == "quit":
print("Thanks for using our program.")
showCart( )
done = True
main( ) 
done = True 
elif ans == "add":
item = input("What would you like to add? ").title( )
addItem(item)
elif ans == "remove":
showCart( )
item = input("What item would you like to remove? ")
.title( )
removeItem(item)
elif ans == "show":
showCart( )
elif ans == "clear":
 clearCart( )
else:
print("Sorry that was not an option.")
main( ) 
