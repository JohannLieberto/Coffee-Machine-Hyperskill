class CoffeeMachine:

    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.money = 550

    def status(self):
        print(f"""
The coffee machine has:
{self.water} of water
{self.milk} of milk
{self.beans} of coffee beans
{self.cups} of disposable cups
${self.money} of money\n""")

    # def resources(self):
    #     if self.water < 400:
    #         print("Sorry, not enough water!\n")
    #         self.choice()
    #     elif self.milk < 540:
    #         print("Sorry, not enough milk!\n")
    #         self.choice()
    #     elif self.beans < 120:
    #         print("Sorry, not enough beans!\n")
    #         self.choice()
    #     else:
    #         pass

    def main(self):
        self.choice()

    def back(self):
        self.choice()

    def coffee_choice(self):
        cc = input("\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")
#        self.resources()
        if cc == "1":
            if self.water > 250 and self.beans > 16:
                print("I have enough resources, making you a coffee!\n")
                self.esp()
                self.choice()
            else:
                print(f"Sorry, not enough water!\n" if self.water < 250 else print("Sorry, not enough milk!\n"))
                self.choice()
        elif cc == "2":
            if self.water > 350 and self.milk > 75 and self.beans:
                print("I have enough resources, making you a coffee!\n")
                self.latte()
                self.choice()
            else:
                print(f"Sorry, not enough water!\n" if self.water < 350 else print("Sorry, not enough milk!\n"))
                self.choice()
        elif cc == "3":
            if self.water > 200 and self.milk > 100 and self.beans > 12:
                print("I have enough resources, making you a coffee!\n")
                self.cappu()
                self.choice()
            else:
                print(f"Sorry, not enough water\n" if self.water < 200 else print("Sorry, not enough milk\n"))
                self.choice()
        elif cc == "back":
            self.back()

    def esp(self):
        self.water -= 250
        self.beans -= 16
        self.money += 4
        self.cups -= 1

    def latte(self):
        self.water -= 350
        self.milk -= 75
        self.beans -= 20
        self.money += 7
        self.cups -= 1

    def cappu(self):
        self.water -= 200
        self.milk -= 100
        self.beans -= 12
        self.money += 6
        self.cups -= 1

    def buy(self):
        self.coffee_choice()

    def fill(self):
        self.water += int(input("\nWrite how many ml of water do you want to add:\n"))
        self.milk += int(input("Write how many ml of milk do you want to add:\n"))
        self.beans += int(input("Write how many grams of coffee beans do you want to add:\n"))
        self.cups += int(input("Write how many disposable cups of coffee do you want to add:\n"))
        # print("\n")
        self.choice()

    def take(self):
        print(f"\nI gave you ${self.money}\n")
        self.money = 0
        self.choice()

    def remaining(self):
        self.status()
        self.choice()

    def choice(self):
        print("Write action buy, fill, take, remaining, exit:")
        choice = input()
        while True:
            if choice == "buy":
                self.buy()
            elif choice == "fill":
                self.fill()
            elif choice == "take":
                self.take()
            elif choice == "remaining":
                self.remaining()
            elif choice == "exit":
                exit()


cofm = CoffeeMachine()
cofm.main()
