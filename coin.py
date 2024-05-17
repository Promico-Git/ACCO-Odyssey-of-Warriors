# create a class to handle the wealth of player       
class Coin():
    def __init__(self,character, max_coin):
        self.character = character
        if character == "Richie":
            max_coin = 150
        elif character == "Jack":
            max_coin = 100
        self.max_coin = max_coin
        self.current_coin = max_coin

    # function that removes from the player wealth when spent
    def spendCoin(self, amount):
        self.current_coin -= amount
        if self.current_coin <=0:
            print(" You are broke bro")

    # function to add to wealth
    def gainCoin(self,amount):
        self.current_coin += amount
        if self.current_coin >= self.max_coin:
            self.current_coin = self.max_coin
            print(" You are at maximum capacity. Coins: " + str(self.current_coin))
        else:
            print(" Gained " + str(amount) + "Coins. Coins: " + str(self.current_coin))

    # display the player wealth
    def displayCoin(self):
        print(" Coins: " + str(self.current_coin))