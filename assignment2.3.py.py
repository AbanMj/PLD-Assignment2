money = int(input("How much money you have?: "))
price_apple = int(input("Price of the apple: "))
max_apple = int(input("how many apple you will buy?(max. of apple is 30 pieces): "))
pay = max_apple * price_apple
change = money - pay
print(f"You can buy {max_apple} apples and your change is {change} ")