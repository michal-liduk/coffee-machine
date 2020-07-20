# Write your code here
class CoffeeMachine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coffee = 120
        self.cups = 9
        self.money = 550

    def user_input(self):
        while True:
            action = input("Write action (buy, fill, take, remaining, exit): ")
            if action == "buy":
                beverage = input(
                    "What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ")
                self.buy(beverage)
            elif action == "fill":
                self.fill()
            elif action == "take":
                self.take()
            elif action == "remaining":
                self.remaining()
            elif action == "exit":
                break

    def buy(self, beverage):
        if beverage == "1":
            if self.water < 250:
                print("Sorry, not enough water!")
            elif self.coffee < 16:
                print("Sorry, not enough coffee!")
            elif self.cups < 1:
                print("Sorry, not enough cups!")
            else:
                self.water = self.water - 250
                self.coffee = self.coffee - 16
                self.money = self.money + 4
                self.cups = self.cups - 1
                print("I have enough resources, making you a coffee!")
        elif beverage == "2":
            if self.water < 350:
                print("Sorry, not enough water!")
            elif self.milk < 75:
                print("Sorry, not enough milk!")
            elif self.coffee < 20:
                print("Sorry, not enough coffee!")
            elif self.cups < 1:
                print("Sorry, not enough cups!")
            else:
                self.water = self.water - 350
                self.milk = self.milk - 75
                self.coffee = self.coffee - 20
                self.money = self.money + 7
                self.cups = self.cups - 1
                print("I have enough resources, making you a coffee!")
        elif beverage == "3":
            if self.water < 200:
                print("Sorry, not enough water!")
            elif self.milk < 100:
                print("Sorry, not enough milk!")
            elif self.coffee < 12:
                print("Sorry, not enough coffee!")
            elif self.cups < 1:
                print("Sorry, not enough cups!")
            else:
                self.water = self.water - 200
                self.milk = self.milk - 100
                self.coffee = self.coffee - 12
                self.money = self.money + 6
                self.cups = self.cups - 1
                print("I have enough resources, making you a coffee!")
        elif beverage == "back":
            pass

    def fill(self):
        self.water = self.water + int(input("Write how many ml of water do you want to add: "))
        self.milk = self.milk + int(input("Write how many ml of milk do you want to add: "))
        self.coffee = self.coffee + int(input("Write how many g of coffee beans do you want to add: "))
        self.cups = self.cups + int(input("Write how many disposable cups of coffee do you want to add :"))

    def take(self):
        print("I gave you $", self.money)
        self.money = 0

    def remaining(self):
        print("The coffee machine has:")
        print(self.water, "of water")
        print(self.milk, "of milk")
        print(self.coffee, "of coffee beans")
        print(self.cups, "of disposable cups")
        print(self.money, "of money")


jacobs = CoffeeMachine()
jacobs.user_input()