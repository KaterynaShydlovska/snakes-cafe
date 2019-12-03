import sys
print("**************************************")
print("**    Welcome to the Snakes Cafe!   **")
print("**    Please see our menu below.    **")
print("**")
print("** To quit at any time, type \"quit\" **")
print("**************************************")

menu = {
    "Appetizers": ["Wings", "Cookies", "Spring Rolls"],
    "Entrees": ["Salmon", "Steak", "Meat Tornado", "A Literal Garden"],
    "Eesserts": ["Ice Cream", "Cake", "Pie"],
    "Drinks": ["Coffee", "Tea", "Unicorn Tears"]
}

for item in menu:
  print('\n')
  print(item)
  print("----------")
  for entree in menu[item]:
    print(entree)
    

print("**************************************")
print("**    What would you like to order?   **")
print("**************************************")


def exit_app():
    sys.exit()


my_order = {}

def make_order():
  answer = input('>')
  if answer == "quit".lower():
    sys.exit()
  else:
    found = False
    for record in menu:
      if answer in menu[record]:
        found = True
    if found:
      if answer in my_order:
        my_order[answer] += 1
      else:
        my_order[answer] = 1
      print(str(my_order[answer]) + " order of " + answer + " have been added to your meal")
      make_order()
    else:
        print('Sorry, we don\'t have that, you can chose something else')
        # make_order()
make_order()





