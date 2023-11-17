import coffee_data as coffee_data
profit = coffee_data.profit


# TODO 1: Check the resources of the coffee machine


# TODO 2: Check the resources sufficient to make the drinking order

def is_drink_sufficient(order_ingredients):
  """Calculates the difference between the resources and clients requirements"""
  for item in order_ingredients:
    if order_ingredients[item] >= coffee_data.resources[item]:
      print(f"Sorry,there isn't enough {item}")
      return False
    
  return True


#TODO 3: Process the coins

def coin_processor():
  """Returns the total calculated coins"""
  print("Please insert coins")
  total = int(input("How many quarters?: "))* 0.25
  total += int(input("How many dimes?: "))* 0.10
  total += int(input("How many nickels?: "))* 0.05
  total += int(input("How many pennies?: "))* 0.01
  
  return total

def transction_successful(recieved, drink_cost):
  """Return Boolean of whether there is enough money"""
  if recieved > drink_cost:
    change = round(recieved - drink_cost, 2)
    print(f"Here is ${change} in change.")
    global profit
    profit += drink_cost
    return True
  else:
    print("Sorry, there is not enough money, Money Refunded")
    return False
  
def make_coffee(name,order_ingredients):
  """Deduct the ingredients"""
  for item in order_ingredients:
    coffee_data.resources[item] -= order_ingredients[item]
  print(f"Here is your {name} ☕")


is_on = True

while is_on:
  choice = input("Which drink would you want? /espresso/ latte/ capucchino/: ")
  if choice == "off":
    is_on = False
  elif choice == "report":
    coffee_data.resources['Money'] = profit
    print(coffee_data.resources)
  else:
    drink = coffee_data.MENU[choice]
    if is_drink_sufficient(drink["ingredients"]):
      payment = coin_processor()
      if transction_successful(payment, drink["cost"]):
        make_coffee(choice, drink["ingredients"])
      
      

