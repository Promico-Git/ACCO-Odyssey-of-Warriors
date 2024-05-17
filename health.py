# Create a class for players health
class Health():
    def __init__(self,character, max_health):
        self.character = character
        if character == "Richie":
            max_health = 100
        elif character == "Jack":
            max_health = 120
        self.max_health = max_health
        self.current_health = max_health

    # function that removes from the player health when called
    def takeDamage(self, amount):
        self.current_health -= amount
        print("You lose "+ str(amount) + "HP")
        if self.current_health <=0:
            #call death function
            endGame()
            sys.exit()


    # function to add to the players health
    def heal(self,amount):
        self.current_health += amount
        if self.current_health >= self.max_health:
            self.current_health = self.max_health
            print(" You are at maximum health. Current health: " + str(self.current_health))
        else:
            print(" Gained " + str(amount) + "hp. Current health: " + str(self.current_health))

    # display health information
    def displayHealth(self):
        print(" Your Current health: " + str(self.current_health))
