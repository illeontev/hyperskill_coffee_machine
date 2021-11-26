class CoffeeMachine:
    WATER_FOR_ESPRESSO = 250
    MILK_FOR_ESPRESSO = 0
    COFFEE_FOR_ESPRESSO = 16
    COST_OF_ESPRESSO = 4

    WATER_FOR_LATTE = 350
    MILK_FOR_LATTE = 75
    COFFEE_FOR_LATTE = 20
    COST_OF_LATTE = 7

    WATER_FOR_CAPUCCINO = 200
    MILK_FOR_CAPUCCINO = 100
    COFFEE_FOR_CAPUCCINO = 12
    COST_OF_CAPUCCINO = 6

    def __init__(self, water, milk, coffee, cups, money):
        self.water_left = water
        self.milk_left = milk
        self.coffee_left = coffee
        self.cups_left = cups
        self.money_left = money
        self.state = "action_chosen"
        print("Write action (buy, fill, take, remaining, exit):")

    def set_init_state(self):
        self.state = "action_chosen"
        print("\nWrite action (buy, fill, take, remaining, exit):")

    def get_command(self, string):
        if self.state == "action_chosen":
            action = string
            if action == "buy":
                print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
                self.state = "type_of_coffee_choose"
            elif action == "fill":
                print("Write how many ml of water you want to add:")
                self.state = "fill_water"
            elif action == "take":
                self.take_money()
                self.set_init_state()
            elif action == "remaining":
                self.print_state()
                self.set_init_state()
            elif action == "exit":
                exit(0)
        elif self.state == "type_of_coffee_choose":
            if string == "back":
                self.set_init_state()
            else:
                self.buy_coffee(int(string))
                self.set_init_state()
        elif self.state == "fill_water":
            self.water_left += int(string)
            print("Write how many ml of milk you want to add:")
            self.state = "fill_milk"
        elif self.state == "fill_milk":
            self.milk_left += int(string)
            print("Write how many grams of coffee beans you want to add:")
            self.state = "coffee_fill"
        elif self.state == "coffee_fill":
            self.coffee_left += int(string)
            print("Write how many disposable coffee cups you want to add:")
            self.state = "cups_fill"
        elif self.state == "cups_fill":
            self.cups_left += int(string)
            self.set_init_state()

    def print_state(self):
        print("The coffee machine has:")
        print(f"{self.water_left} of water")
        print(f"{self.milk_left} of milk")
        print(f"{self.coffee_left} of coffee beans")
        print(f"{self.cups_left} of disposable cups")
        print(f"${self.money_left} of money")

    def make_capuccino(self):
        if self.water_left < CoffeeMachine.WATER_FOR_CAPUCCINO:
            print("Sorry, not enough water!")
            return
        if self.milk_left < CoffeeMachine.MILK_FOR_CAPUCCINO:
            print("Sorry, not enough milk!")
            return
        if self.coffee_left < CoffeeMachine.COFFEE_FOR_CAPUCCINO:
            print("Sorry, not enough coffee!")
            return
        if self.cups_left < 1:
            print("Sorry, not enough cups!")
            return

        print("I have enough resources, making you a coffee!")

        self.water_left -= CoffeeMachine.WATER_FOR_CAPUCCINO
        self.milk_left -= CoffeeMachine.MILK_FOR_CAPUCCINO
        self.coffee_left -= CoffeeMachine.COFFEE_FOR_CAPUCCINO
        self.cups_left -= 1
        self.money_left += CoffeeMachine.COST_OF_CAPUCCINO

    def make_latte(self):
        if self.water_left < CoffeeMachine.ATER_FOR_LATTE:
            print("Sorry, not enough water!")
            return
        if self.milk_left < CoffeeMachine.MILK_FOR_LATTE:
            print("Sorry, not enough milk!")
            return
        if self.coffee_left < CoffeeMachine.COFFEE_FOR_LATTE:
            print("Sorry, not enough coffee!")
            return
        if self.cups_left < 1:
            print("Sorry, not enough cups!")
            return

        print("I have enough resources, making you a coffee!")

        self.water_left -= CoffeeMachine.WATER_FOR_LATTE
        self.milk_left -= CoffeeMachine.MILK_FOR_LATTE
        self.coffee_left -= CoffeeMachine.COFFEE_FOR_LATTE
        self.cups_left -= 1
        self.money_left += CoffeeMachine.COST_OF_LATTE

    def make_espresso(self):
        if self.water_left < CoffeeMachine.WATER_FOR_ESPRESSO:
            print("Sorry, not enough water!")
            return
        if self.milk_left < CoffeeMachine.MILK_FOR_ESPRESSO:
            print("Sorry, not enough milk!")
            return
        if self.coffee_left < CoffeeMachine.COFFEE_FOR_ESPRESSO:
            print("Sorry, not enough coffee!")
            return
        if self.cups_left < 1:
            print("Sorry, not enough cups!")
            return

        print("I have enough resources, making you a coffee!")

        self.water_left -= CoffeeMachine.WATER_FOR_ESPRESSO
        self.milk_left -= CoffeeMachine.MILK_FOR_ESPRESSO
        self.coffee_left -= CoffeeMachine.COFFEE_FOR_ESPRESSO
        self.cups_left -= 1
        self.money_left += CoffeeMachine.COST_OF_ESPRESSO

    def buy_coffee(self, type_of_drink):
        if type_of_drink == 1:
            self.make_espresso()
        elif type_of_drink == 2:
            self.make_latte()
        elif type_of_drink == 3:
            self.make_capuccino()

    def take_money(self):
        if self.money_left > 0:
            print(f"I gave you ${self.money_left}")
            self.money_left = 0

while True:
    machine = CoffeeMachine(400, 540, 120, 9, 550)
    while True:
        machine.get_command(input())
