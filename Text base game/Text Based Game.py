import random #I have my imports at the top of my project
import time
import sys

Parts = ["Stock", "Barrel", "Trigger group", "Sight", "Reciever"] #These are my resources in the game

#testing inventory
#inventory = ["Barrel", "Barrel", "Barrel", "Barrel", "Stock", "Stock", "Stock", "Stock", "Reciever", "Reciever", "Reciever", "Reciever", "Reciever", "Trigger group", "Trigger group", "Trigger group", "Trigger group", "Sight", "Sight", "Sight", "Sight", "Sight", "Sight", "Sight",]
inventory = [] #this list is edited as the game progresses.

def collect(part): #This function allows you to put parts into your inventory or leave them behind.
    print(">>")
    print(f"You found a {part}.")
    print("Would you like to take it with you?")
    print("Y:              1")
    print("")
    print("N:              0")
    print("")
    print("Stop searching: 5")
    print("")
    choice = int(input('> '))
    choice
    if choice == 1:
        inventory.append(part)
        print(">>")
        print(f"You placed the {part} in your bag.")
        time.sleep(2)
    elif choice == 0:
        print(">>")
        print(f"You left the {part} behind.")
        time.sleep(2) #I felt like adding a delay between input and result makes it fell more like a game.
    elif choice == 5:
        Next_move()
    else:
        error()
        collect(part)


def error(): #A general purpose error message function to avoid the game breaking.
    print(">>")
    print("Please use a valid input.")

def searching(): #This function decides what part will be found in each building.
    item = random.randint(1, 100)
    if item <= 39:
        collect(Parts[0])
    elif item <= 69:
        collect(Parts[1])
    elif item <= 89:
        collect(Parts[2])
    elif item <= 97:
        collect(Parts[3])
    else:
        collect(Parts[4])

def prompt(): #This is the function that prompts the player to collect parts
    global inventory
    num_buildings = random.randint(1, 12)
    print(">>")
    print(f'You find yourself looking at {num_buildings} buildings; how many would you like to search?')
    print("")
    choice = int(input())
    time.sleep(2)
    if choice == 0:
        print(">>")
        print("You did not search any buildings")
        Next_move()
    buildings = choice + 1
    if choice > num_buildings:
        print(">>")
        print("There are not that many buildings.")
        prompt()
    for x in range(1, buildings):
        searching()
    Next_move()
            #time.sleep(10)

def Next_move(): #This is my menu apart from the main menu. you cannot quit from here.
    print(">>")
    print("What will you do now?")
    print("Look for new buildings: 1")
    print("Manage Inventory:       2")
    print("Craft a weapon:         3")
    print("")
    print("Main Menu:              4")
    print("")
    choice = int(input('> '))
    if choice == 1:
        prompt()
    elif choice == 2:
        print(">>")
        print("You find this in your bag")
        inventory_man()
    elif choice == 3:
            crafting()
    elif choice == 4:
        Main_Menu()

def inventory_man(): #This function allows you to edit the inventory list
    print(inventory)
    print("Would you like to drop something?")
    print("Y: 1")
    print("N: 0")
    print("")
    edit = int(input("> "))
    if edit == 1:
        print(">>")
        print(inventory)
        print("Drop Item:       1")
        print("Clear inventory: 2")
        print("Plan next move:  3")
        print("")
        selec = int(input("> "))
        selec
        if selec == 1:
            print(">>")
            print("What index do you want to manage?")
            print("")
            item = inventory[int(input("> "))]
            print(f"Would you like to drop {item}?")
            print("Y: 1")
            print("N: 0")
            print("")
            action = int(input("> "))
            if action == 1:
                inventory.remove(item)
                print(">>")
                print(f"You dropped the {item}.")
                print(inventory)
                print('Would you like to further edit your inventory?')
                print("Y: 1")
                print("N: 0")
                print("")
                choice = int(input('> '))
                choice
                if choice == 1:
                    inventory_man()
                elif choice == 0:
                    print(">>")
                    print("You put your bag away")
                    Next_move()
                else:
                    error()
                    inventory_man()
            elif action == 0:
                print(">>")
                print(f"You put the {item} back in your bag")
                print("Continue editing inventory: 1")
                print("Plan your next move:        2")
                print("")
                selec1 = int(input("> "))
                selec1
                if selec1 == 1:
                    inventory_man()
                elif selec1 == 2:
                    Next_move()
                else:
                    error()
                    inventory_man()
            else:
                error()
                inventory_man()
        elif selec == 2:
            inventory.clear()
            print(">>")
            print("You emptied your bag.")
            Next_move()
        elif selec == 3:
            Next_move()
        else:
            error()
            inventory_man()
    elif edit == 0:
        Next_move()
    else:
        error()
        inventory_man()



def craft_rifle():
    inventory.remove("Stock")
    inventory.remove("Barrel")
    inventory.remove("Trigger group")
    inventory.remove("Sight")
    inventory.remove("Sight")
    inventory.remove("Reciever")
    inventory.append("Rifle")
    print(">>")
    print("You assembled a Rifle!")
    print(inventory)
    print("Would you like to craft something else?")
    print("Y: 1")
    print("")
    print("N: 0")
    print("")

def craft_handgun():
    inventory.remove("Barrel")
    inventory.remove("Trigger group")
    inventory.remove("Sight")
    inventory.remove("Sight")
    inventory.remove("Reciever")
    inventory.append("Handgun")
    print(">>")
    print("You assembled a Handgun!")
    print(inventory)
    print("Would you like to craft something else?")
    print("Y: 1")
    print("N: 0")
    print("")

def craft_shotgun():
    inventory.remove("Stock")
    inventory.remove("Barrel")
    inventory.remove("Trigger group")
    inventory.remove("Sight")
    inventory.remove("Reciever")
    inventory.append("Shotgun")
    print(">>")
    print("You assembled a Shotgun!")
    print(inventory)
    print("Would you like to craft something else?")
    print("Y: 1")
    print("N: 0")
    print("")

def craft_ar():
    inventory.remove("Stock")
    inventory.remove("Barrel")
    inventory.remove("Trigger group")
    inventory.remove("Sight")
    inventory.remove("Sight")
    inventory.remove("Reciever")
    inventory.remove("Reciever")
    inventory.append("AR-15")
    print(">>")
    print("You assembled an AR-15!!!")
    print("How did you find this easter egg!? :D")
    print(inventory)
    print("Would you like to craft something else?")
    print("Y: 1")
    print("N: 0")
    print("")

def rifle_recipe():
    print(">>")
    print("Rifle:")
    print("1 Stock")
    print("1 Barrel")
    print("1 Trigger group")
    print("2 Sights")
    print("1 Reciever")
    time.sleep(5)
    crafting()

def handgun_recipe():
    print(">>")
    print("Handgun:")
    print("1 Barrel")
    print("1 Trigger group")
    print("2 Sights")
    print("1 Reciever")
    time.sleep(5)
    crafting()

def shotgun_recipe():
    print(">>")
    print("Shotgun")
    print("1 Stock")
    print("1 Barrel")
    print("1 Trigger group")
    print("1 Sight")
    print("1 Reciever")
    time.sleep(5)
    crafting()

def all_recipes():
    print(">>")
    print("Rifle:")
    print("1 Stock")
    print("1 Barrel")
    print("1 Trigger group")
    print("2 Sights")
    print("1 Reciever")
    print("Handgun:")
    print("1 Barrel")
    print("1 Trigger group")
    print("2 Sights")
    print("1 Reciever")
    print("Shotgun")
    print("1 Stock")
    print("1 Barrel")
    print("1 Trigger group")
    print("1 Sight")
    print("1 Reciever")
    time.sleep(5)
    crafting()

def crafting(): #This function determins the logic of crafting.
    print(">>")
    print("Would you like to craft?:   1")
    print("          Or,")
    print("Refrence crafting recipes?: 2")
    print("")
    print("Stop crafting:              3")
    print("")
    choice = int(input("> "))
    choice
    if choice == 1:
        print(">>")
        print("What would you like to craft?")
        print("Rifle:           1")
        print("Handgun:         2")
        print("Shotgun:         3")
        print("")
        print("Stop crafting:   4")
        print("")
        choice1 = int(input("> "))
        choice1
        if choice1 == 1:
            craft_rifle()
            choice2 = int(input("> "))
            if choice2 == 1:
                crafting()
            elif choice2 == 0:
                Next_move()
            else:
                error()
                crafting()
        elif choice1 == 2:
            craft_handgun()
            choice2 = int(input("> "))
            if choice2 == 1:
                crafting()
            elif choice2 == 0:
                Next_move()
            else:
                error()
                crafting()
        elif choice1 == 3:
            craft_shotgun()
            choice2 = int(input("> "))
            if choice2 == 1:
                crafting()
            elif choice2 == 0:
                Next_move()
            else:
                error()
                crafting()
        elif choice1 == 4:
            crafting()
        elif choice1 == 421: #If you input the number of my old squadron then you will get a special gun! granted you have the materials...
            craft_ar()
            choice2 = int(input("> "))
            if choice2 == 1:
                crafting()
            elif choice2 == 0:
                Next_move()
            else:
                error()
                crafting()
    elif choice == 2:
        reference()
    elif choice == 3:
        print(">>")
        print("You left your workshop")
        Next_move()
    else:
        error()
        crafting()

def reference(): #I forked this part of the crafting function into it's own function for ease of reading.
    print(">>")
    print("What recipe do you want to refrence?")
    print("Rifle:                               1")
    print("Handgun:                             2")
    print("Shotgun:                             3")
    print("Display all:                         4")
    print("")
    print("I don't need a reference right now.: 5")
    choice3 = int(input("> "))
    choice3
    if choice3 == 1:
        rifle_recipe()
    elif choice3 == 2:
        handgun_recipe()
    elif choice3 == 3:
        shotgun_recipe()
    elif choice3 == 4:
        all_recipes()
    elif choice3 == 5:
        crafting()

def Main_Menu(): #My main menu. Simple but effective. You must be here to quit the game.
    print('START: 1')
    print('Exit:  5')
    menu_choice = int(input('> '))
    if menu_choice == 1:
        prompt()
    elif menu_choice == 5:
        end_game()
    else:
        error()
        Main_Menu()

def end_game(): #A general purpose function to end the game properly.
    print('"God speed Spiderman"')
    sys.exit()

#My whole game can be accessed by calling this single function.
Main_Menu()
