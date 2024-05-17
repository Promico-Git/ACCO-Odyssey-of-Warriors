import random
import sys
from backpack import Backpack
from health import Health
from coin import Coin
from monster import Monster, Room


def endGame():
    print("You died better luck next time")
def exit(): 
    print("Seems you were lied to. You are now stuck in a void forever")

def character(actor): 
    print("You are", actor)

def store(player_backPack):
    #player_backPack = Backpack()

    print("You are in the store") 
    print("Prepare for the task ahead, you have been given _------")
    count = 2 
    list = [] 
    while count>0: 
        backPack = player_backPack.itemList()
        if "Hammer" not in backPack:
            print(" Press [1] to acquire a Hammer")
            list.append(1)

        if "Die" not in backPack:
            print(" Press [2] to acquire a Die")
            list.append(2)

        if "Compass" not in backPack:
            print(" Press [3] to acquire a Compass")
            list.append(3)

        if "Mystery Box" not in backPack:
            print(" Press [4] to acquire a Mystery Box")
            list.append(4)

        choice = int(input("\nChoice"))
        if choice in list:
            if choice == 1:
                player_backPack.addItem("Hammer")
                list.remove(1)
                print("You have acquired a Hammer\n")
            if choice == 2:
                player_backPack.addItem("Die")
                list.remove(2)
                print("You have acquired a Die\n")
            if choice == 3:
                player_backPack.addItem("Compass")
                list.remove(3)
                print("You have acquired a Compass\n")
            if choice == 4:
                player_backPack.addItem("Mystery Box")
                list.remove(4)
                print("You have acquired a Mystery Box\n")

            count-=1
            #list = []
    print("You will be sent to a random location to face your foe")

def battle(monster, player, backPack):
    while player.current_health > 1 and monster.health >1:
            ## Player attack
            print("What is your weapon of choice?\n")
            if "Hammer" in backPack.itemList():
                hammer = "[Available]"            
            else: hammer = "[Unavailable]"
            if "Die" in backPack.itemList():
                dice = "[Available]"
            else: dice = "[Unavailable]"

            if "Mystery Box" in backPack.itemList():
                box = "[Available]"                
            else: box = "[Unavailable]"


            print("\n Press [1] to use Hammer "+hammer)
            print(" Press [2] to use Die "+dice)
            print(" Press [3] to use Mystery Box "+box)
            print(" Press [4] to use own strength")
            choice = int(input(""))
            if choice == 1 and hammer == "[Available]":
                backPack.removeItem("Hammer")
                monster.takeDamage(75)
                player.displayHealth()
                monster.displayInfo()
            elif choice == 2 and dice == "[Available]":
                backPack.removeItem("Die")
                die_number = random.randint(1,6)
                if die_number == 6:
                    print(" You rolled a 6.\n Monster loses 100HP")
                    monster.takeDamage(100)
                elif die_number == 5:
                    print(" You rolled a 5.\n Monster loses 80HP")
                    monster.takeDamage(80)
                elif die_number == 4:
                    print(" You rolled a 4.\n Monster loses 60HP")
                    monster.takeDamage(60)
                elif die_number == 3:
                    print(" You rolled a 3.\n Monster loses 40HP")
                    monster.takeDamage(40)
                elif die_number == 2:
                    print(" You rolled a 2.\n Monster loses 20HP")
                    monster.takeDamage(20)
                elif die_number == 1:
                    print(" You rolled a 1.\n Bad luck.\n You lose 100HP")
                    player.takeDamage(100)
                player.displayHealth()
                monster.displayInfo()
            elif choice == 3 and box == "[Available]":
                backPack.removeItem("Mystery Box")
                mysteryBox(backPack)                
                continue
            elif choice == 4:
                monster.takeDamage(30)
                player.takeDamage(20)
                player.displayHealth()
                monster.displayInfo()
            elif choice not in [1,2,3,4]: 
                print(" No weapon selected, try again")
                continue
            else: 
                print(" Selected weapon not available")
                continue

            ##Monster attack

            if monster.health >1:
                print("\nMonster attacked!!!")
                attack_type = random.randint(1,3)
                if attack_type == 1:
                    player.takeDamage(monster.attack)
                else:
                    ##escape room
                    escapeRoom(monster, player, backPack)

                player.displayHealth()
                monster.displayInfo()
            else: print(" You have defeated the monster")

# define the mystery box
def mysteryBox(player_backPack):
    list = []
    while len(list) == 0:
        mystery_list = ["Hammer","Die","Compass","Nothing"]
        item = random.choice(mystery_list)
        if item not in player_backPack.itemList():
            if item in ["Hammer","Die","Compass"]:
                player_backPack.addItem(item)
                list.append(item)
                print(" Mystery Box added: "+ item)
            else: print(" Mystery Box added nothing")

# define the monsters escape roon    
def escapeRoom(monster, player, backPack):
    print("Oops, you have been trapped in an enclosed box. There are two doors to choose from. Pick the wrong door and you lose some of you life. Choose the right door and you do damage to the monster.")
    print("Josephine: 'Use a compass. It will guide you'")
    if "Compass" in backPack.itemList():
        compass = "[Available]"                
    else: compass = "[Unavailable]"

    check = []
    while len(check) == 0:
        print(" \n Press [1] to use Compass "+compass)
        print(" Press [2] to use the door on the right")
        print(" Press [3] to use the door on the left")
        choice = int(input(""))
        if choice == 1 and compass == "[Available]":
            backPack.removeItem("Compass")
            print(" You used a compass and went through the correct door, Now monster takes 20HP damage to life")
            monster.takeDamage(20)
            check.append(1)
        elif choice == 2 or choice == 3:
            list = random.randint(1,2)
            if list == 1:
                print(" You went through the correct door, you escaped without any damage")
            elif list == 2:
                print(" You chose the wrong door, you take 50HP damage")
                player.takeDamage(50)
                player.displayHealth()
                monster.displayInfo()
            check.append(1)
        elif choice not in [1,2,3]: 
            print(" No option selected, try again")
            continue
        else: 
            print(" Compass not available")
            continue

def main(): 
    print("You awaken in a strange white room, You see nothing but two doors in opposite directions.")
    print("On the red door 'Escape' is written, on the green door 'Trials' is written")
    print("A voice comes up saying 'Finally it is up, it is awake'")
    print("Gojo: 'I am Gojo, welcome to the waiting room, behind you there is a red door, the door leads to your freedom.")
    print("In front of you there is a green door, the door leads to a path of trial to test your courage and wisdom")
    print("Choose wisely'")
    option = int(input("\nPress [1] to use the Red Door. \nPress [2] to use the Green Door.\n")) 
    if option == 1: 
        exit() 
    elif option == 2:
        print("Josephine: 'Hii, I am Josephine. I will be your guide. \nWelcome to the store, to continue, select a character")
        character_selection = int(input("\nPress [1] to play as Richie. [Health:100HP, Coin:150] \nPress [2] to play as Jack.[Health:120HP, Coin:100]\n")) 
        if character_selection == 1: 
            player = "Richie" 
        elif character_selection == 2: 
            player = "Jack" 
        else: 
            print("Try that again") 
        character(player)
        print("\nYou are at full health and wealth")
        player_health = Health(player,0)
        player_health.displayHealth()
        player_coin = Coin(player,0)
        player_coin.displayCoin()

        backPack = Backpack()

        # Face the first monster
        store(backPack)

        availability = ""
        hammer = ""
        dice = ""
        compass = ""
        box = ""


        monster1 = Monster("Goblin",10,100)

        print("Welcome to your first challenge, your foe is a Goblin. " + 
        "It has its life at 100HP with an attack dealing 10HP damage.\nIt has a soft underbelly and uses escape rooms as its main weapon.\n ")
        monster1.displayInfo()
        print("\nYou attack first. ")
        battle(monster1,player_health, backPack)

        # Face the second monster
        store(backPack)
        monster2 = Monster("Orc",20,120)
        print("Welcome to your next challenge, your foe is an Orc. " + 
        "It has its life at 120HP with an attack dealing 20HP damage.\nIt has a moderately hard underbelly and uses raw strength as its main weapon.\n ")
        monster2.displayInfo()
        print("\nYou attack first. ")
        battle(monster2,player_health, backPack)


        # Face the third monster
        store(backPack)
        monster3 = Monster("Dragon",30,150)
        print("Welcome to your final challenge, your foe is a Dragon. " + 
        "It has its life at 150HP with an attack dealing 30HP damage.\nIt has an extremely hard underbelly and uses random attacks.\n ")
        monster3.displayInfo()
        print("\nYou attack first. ")
        battle(monster3,player_health, backPack)

        print("You won the game")


    else: 
        print("Try that again")

if __name__ == "__main__": 
    main()