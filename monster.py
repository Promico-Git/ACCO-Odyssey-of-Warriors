 # class to hold data of monster and control monster       
class Monster():
    def __init__(self,name,attack,health):
        self.name = name
        self.attack = attack
        self.health = health
    def displayInfo(self):
        print("Monster stats:")
        print(" Monster: "+self.name+"\n Attack: "+str(self.attack)+"\n Health: "+str(self.health))
    def takeDamage(self, amount):
        self.health -= amount
        print("Monster loses "+ str(amount) + "HP")
        if self.health <=0:
            #call death function
            print("Monster is dead")

class Room():
    def roomOne(self,backPack):
        backPack = Backpack()
