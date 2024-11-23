import random #I have my imports at the top of my project
import time
import sys

Parts = ["Stock", "Barrel", "Trigger group", "Sight", "Reciever"] #These are my resources in the game

#testing inventory
#inventory = ["Barrel", "Barrel", "Barrel", "Barrel", "Stock", "Stock", "Stock", "Stock", "Reciever", "Reciever", "Reciever", "Reciever", "Reciever", "Trigger group", "Trigger group", "Trigger group", "Trigger group", "Sight", "Sight", "Sight", "Sight", "Sight", "Sight", "Sight",]
inventory = [] #this list is edited as the game progresses.
collection = [] #This list is related to displaying what you found after each search.

def collect(part): #This function allows you to put parts into your inventory or leave them behind.
    print(">>")
    print(f"You found a {part}.")
    print("Would you like to take it with you?")
    print("")
    print("Y / N")
    print("")
    print(f'Stop searching: "S"')
    print("")
    answer = str(input('> '))
    answer
    if answer == 'Y':
        inventory.append(part)
        collection.append(part)
        print(">>")
        print(f"You placed the {part} in your bag.")
        time.sleep(2)
    elif answer == 'y':
        inventory.append(part)
        collection.append(part)
        print(">>")
        print(f"You placed the {part} in your bag.")
        time.sleep(2)
    elif answer == 'N':
        print(">>")
        print(f"You left the {part} behind.")
        time.sleep(2) #I felt like adding a delay between input and result makes it fell more like a game.
    elif answer == 'n':
        print(">>")
        print(f"You left the {part} behind.")
        time.sleep(2) #I felt like adding a delay between input and result makes it fell more like a game.
    elif answer == 'S':
        Next_move()
    elif answer == 's':
        track_collection()
        Next_move()
    elif answer == int(input()):
        error()
        answer
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
    track_collection()
    Next_move()

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

def track_collection(): #I was able to re-use and modify my track_inventory function.
    print(">>")
    print("The haul from your efforts.")
    print('')
    if 'Stock' in collection:
        if collection.count('Stock') == 1:
            print(f'{collection.count('Stock')} Stock')
        elif collection.count('Stock') > 1:
            print(f'{collection.count('Stock')} Stocks')
    if 'Barrel' in collection:
        if collection.count('Barrel') == 1:
            print(f'{collection.count('Barrel')} Barrel')
        elif collection.count('Barrel') > 1:
            print(f'{collection.count('Barrel')} Barrels')
    if 'Trigger group' in  collection:
        if collection.count('Trigger group') == 1:
            print(f'{collection.count('Trigger group')} Trigger group')
        elif collection.count('Trigger group') > 1:
            print(f'{collection.count('Trigger group')} Trigger groups')
    if 'Sight' in  collection:
        if collection.count('Sight') == 1:
            print(f'{collection.count('Sight')} individual sight')
        elif collection.count('Sight') > 1:
            print(f'{collection.count('Sight')} individual sights')
    if 'Reciever' in  collection:
        if collection.count('Reciever') == 1:
            print(f'{collection.count('Reciever')} Reciever')
        elif collection.count('Reciever') > 1:
            print(f'{collection.count('Reciever')} Recievers')
    collection.clear()

def track_inventory():
    if 'Stock' in inventory:
        if inventory.count('Stock') == 1:
            print(f'You have {inventory.count('Stock')} Stock')
        elif inventory.count('Stock') > 1:
            print(f'You have {inventory.count('Stock')} Stocks')
    if 'Barrel' in inventory:
        if inventory.count('Barrel') == 1:
            print(f'You have {inventory.count('Barrel')} Barrel')
        elif inventory.count('Barrel') > 1:
            print(f'You have {inventory.count('Barrel')} Barrels')
    if 'Trigger group' in  inventory:
        if inventory.count('Trigger group') == 1:
            print(f'You have {inventory.count('Trigger group')} Trigger group')
        elif inventory.count('Trigger group') > 1:
            print(f'You have {inventory.count('Trigger group')} Trigger groups')
    if 'Sight' in  inventory:
        if inventory.count('Sight') == 1:
            print(f'You have {inventory.count('Sight')} individual sight')
        elif inventory.count('Sight') > 1:
            print(f'You have {inventory.count('Sight')} individual sights')
    if 'Reciever' in  inventory:
        if inventory.count('Reciever') == 1:
            print(f'You have {inventory.count('Reciever')} Reciever')
        elif inventory.count('Reciever') > 1:
            print(f'You have {inventory.count('Reciever')} Recievers')
    if 'Rifle' in  inventory:
        if inventory.count('Rifle') == 1:
            print(f'You have {inventory.count('Rifle')} Rifle')
        elif inventory.count('Rifle') > 1:
            print(f'You have {inventory.count('Rifle')} Rifles')
    if 'Handgun' in  inventory:
        if inventory.count('Handgun') == 1:
            print(f'You have {inventory.count('Handgun')} Handgun')
        elif inventory.count('Handgun') > 1:
            print(f'You have {inventory.count('Handgun')} Handguns')
    if 'Shotgun' in  inventory:
        if inventory.count('Shotgun') == 1:
            print(f'You have {inventory.count('Shotgun')} Shotgun')
        elif inventory.count('Shotgun') > 1:
            print(f'You have {inventory.count('Shotgun')} Shotguns')
    if 'AR-15' in  inventory:
        if inventory.count('AR-15') == 1:
            print(f'You have {inventory.count('AR-15')} AR-15')
        elif inventory.count('AR-15') > 1:
            print(f'You have {inventory.count('AR-15')} AR-15s')

def inventory_man(): #This function allows you to edit the inventory list
    print('>>')
    track_inventory()
    print("Would you like to drop something?")
    print("Y / N")
    print("")
    edit = str(input("> "))
    if edit == 'Y':
        print(">>")
        track_inventory()
        print("Drop Item:       1")
        print("Clear inventory: 2")
        print("Plan next move:  3")
        print("")
        selec = int(input("> "))
        selec
        if selec == 1:
            print(">>")
            print("What type of part do you want to manage?")
            print("Valid Inputs(case sensitive): Stock, Barrel, Trigger group, Sight, Reciever")
            print("")
            k = inventory
            x = k.index(str(input()))
            item = inventory[x]
            print(f"Would you like to drop a {item}?")
            print("Y / N")
            print("")
            action = str(input("> "))
            if action == 'Y':
                inventory.remove(item)
                print(">>")
                print(f"You dropped one of the {item}s.")
                track_inventory()
                print('Would you like to further edit your inventory?')
                print("Y / N")
                print("")
                choice = str(input('> '))
                choice
                if choice == 'Y':
                    inventory_man()
                if choice == 'y':
                    inventory_man()
                elif choice == 'N':
                    print(">>")
                    print("You put your bag away")
                    Next_move()
                elif choice == 'n':
                    print(">>")
                    print("You put your bag away")
                    Next_move()
                elif choice == int:
                    error()
                    choice
                else:
                    error()
                    choice
            if action == 'y':
                inventory.remove(item)
                print(">>")
                print(f"You dropped one of the {item}s.")
                track_inventory()
                print('Would you like to further edit your inventory?')
                print("Y / N")
                print("")
                choice = str(input('> '))
                choice
                if choice == 'Y':
                    inventory_man()
                if choice == 'y':
                    inventory_man()
                elif choice == 'N':
                    print(">>")
                    print("You put your bag away")
                    Next_move()
                elif choice == 'n':
                    print(">>")
                    print("You put your bag away")
                    Next_move()
                elif choice == int:
                    error()
                    choice
                else:
                    error()
                    choice
            elif action == 'N':
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
                elif selec1 == str:
                    error()
                    selec1
                else:
                    error()
                    selec1
            elif action == 'n':
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
                elif selec1 == str:
                    error()
                    selec1
                else:
                    error()
                    selec1
            elif action == int:
                error()
                action
            else:
                error()
                action
        elif selec == 2:
            print("Are you sure you want to empty your bag?")
            print("This cannot be undone.")
            delete = str(input('> '))
            delete
            if delete == 'y':
                inventory.clear()
                print(">>")
                print("You emptied your bag.")
                Next_move()
            elif delete == 'Y':
                inventory.clear()
                print(">>")
                print("You emptied your bag.")
                Next_move()
            elif delete == 'N':
                inventory_man()
            elif delete == 'n':
                inventory_man()
        elif selec == 3:
            Next_move()
        elif selec == str:
            error()
            selec
        else:
            error()
            selec
    if edit == 'y':
        print(">>")
        track_inventory()
        print("Drop Item:       1")
        print("Clear inventory: 2")
        print("Plan next move:  3")
        print("")
        selec = int(input("> "))
        selec
        if selec == 1:
            print(">>")
            print("What type of part do you want to manage?")
            print("")
            k = inventory
            x = k.index(str(input()))
            item = inventory[x]
            print(f"Would you like to drop a {item}?")
            print("Y / N")
            print("")
            action = str(input("> "))
            if action == 'Y':
                inventory.remove(item)
                print(">>")
                print(f"You dropped one of the {item}s.")
                track_inventory()
                print('Would you like to further edit your inventory?')
                print("Y / N")
                print("")
                choice = str(input('> '))
                choice
                if choice == 'Y':
                    inventory_man()
                if choice == 'y':
                    inventory_man()
                elif choice == 'N':
                    print(">>")
                    print("You put your bag away")
                    Next_move()
                elif choice == 'n':
                    print(">>")
                    print("You put your bag away")
                    Next_move()
                elif choice == int:
                    error()
                    choice
                else:
                    error()
                    choice
            if action == 'y':
                inventory.remove(item)
                print(">>")
                print(f"You dropped one of the {item}s.")
                track_inventory()
                print('Would you like to further edit your inventory?')
                print("Y / N")
                print("")
                choice = str(input('> '))
                choice
                if choice == 'Y':
                    inventory_man()
                if choice == 'y':
                    inventory_man()
                elif choice == 'N':
                    print(">>")
                    print("You put your bag away")
                    Next_move()
                elif choice == 'n':
                    print(">>")
                    print("You put your bag away")
                    Next_move()
                elif choice == int:
                    error()
                    choice
                else:
                    error()
                    choice
            elif action == 'N':
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
                elif selec1 == str:
                    error()
                    selec1
                else:
                    error()
                    selec1
            elif action == 'n':
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
                elif selec1 == str:#endday msg play game and see if you can find any issues with current systems. 
                    error()
                    selec1
                else:
                    error()
                    selec1
            elif action == int:
                error()
                action
            else:
                error()
                action
        elif selec == 2:
            inventory.clear()
            print(">>")
            print("You emptied your bag.")
            Next_move()
        elif selec == 3:
            Next_move()
        elif selec == str:
            error()
            selec
        else:
            error()
            selec
    elif edit == 'N':
        Next_move()
    elif edit == 'n':
        Next_move()
    elif edit == str:
        error()
        edit
    else:
        error()
        inventory_man()


def check_inv(value):
    if (value in inventory):
        return True
    else:
        return False

def check_sights(value):
    if inventory.count(value) >= 2:
        return True
    else:
        return False

#Something is wrong witht the crafting fucntion. 


def check_rifle():
    check_inv('Stock')
    check_inv('Barrel')
    check_inv('Trigger group')
    check_sights('Sight')
    check_inv('Reciever')
    if check_inv('Stock') and check_inv('Barrel') and check_inv('Trigger group') and check_sights('Sight') and check_inv('Reciever') == True:
        return True
    if check_inv('Stock') and check_inv('Barrel') and check_inv('Trigger group') and check_sights('Sight') and check_inv('Reciever') == False:
        return False

def check_handgun():
    check_inv('Barrel')
    check_inv('Trigger group')
    check_sights('Sight')
    check_inv('Reciever')
    if check_inv('Barrel') and check_inv('Trigger group') and check_sights('Sight') and check_inv('Reciever') == True:
        return True
    if check_inv('Barrel') and check_inv('Trigger group') and check_sights('Sight') and check_inv('Reciever') == False:
        return False

def check_shotgun():
    check_inv('Stock')
    check_inv('Barrel')
    check_inv('Trigger group')
    check_inv('Sight')
    check_inv('Reciever')
    if check_inv('Stock') and check_inv('Barrel') and check_inv('Trigger group') and check_inv('Sight') and check_inv('Reciever') == True:
        return True
    if check_inv('Stock') and check_inv('Barrel') and check_inv('Trigger group') and check_inv('Sight') and check_inv('Reciever') == False:
        return False

def check_AR():
    check_inv('Stock')
    check_inv('Barrel')
    check_inv('Trigger group')
    check_sights('Sight')
    check_inv('Reciever')
    if check_inv('Stock') and check_inv('Barrel') and check_inv('Trigger group') and check_sights('Sight') and check_sights('Reciever') == True:
        return True
    if check_inv('Stock') and check_inv('Barrel') and check_inv('Trigger group') and check_sights('Sight') and check_sights('Reciever') == False:
        return False


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
    track_inventory()
    print('')
    print("Would you like to craft something else?")
    print("Y / N")
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
    track_inventory()
    print('')
    print("Would you like to craft something else?")
    print("Y / N")
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
    track_inventory()
    print('')
    print("Would you like to craft something else?")
    print("Y / N")
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
    track_inventory()
    print('')
    print("Would you like to craft something else?")
    print("Y / N")
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
    print('')
    print("          Or,")
    print('')
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
            check_rifle()
            if check_rifle() == True:
                craft_rifle()
                choice2 = str(input("> "))
                if choice2 == 'Y':
                    crafting()
                elif choice2 == 'y':
                    crafting()
                elif choice2 == 'N':
                    Next_move()
                elif choice2 == 'n':
                    Next_move()
                elif choice2 == int:
                    error()
                    choice2
                else:
                    error()
                    choice2
            else:
                print("You do not have all of the needed parts")
                crafting()
        elif choice1 == 2:
            check_handgun()
            if check_handgun() == True:
                craft_handgun()
                choice2 = str(input("> "))
                if choice2 == 'Y':
                    crafting()
                elif choice2 == 'y':
                    crafting()
                elif choice2 == 'N':
                    Next_move()
                elif choice2 == 'n':
                    Next_move()
                elif choice2 == int:
                    error()
                    choice2
                else:
                    error()
                    choice2
            else:
                print("You do not have all of the needed parts")
                crafting()
        elif choice1 == 3:
            check_shotgun()
            if check_shotgun() == True:
                craft_shotgun()
                choice2 = str(input("> "))
                if choice2 == 'Y':
                    crafting()
                elif choice2 == 'y':
                    crafting()
                elif choice2 == 'N':
                    Next_move()
                elif choice2 == 'n':
                    Next_move()
                elif choice2 == int:
                    error()
                    choice2
                else:
                    error()
                    choice2
            else:
                print("You do not have all of the needed parts")
                crafting()
        elif choice1 == 4:
            crafting()
        elif choice1 == 421: #If you input the number of my old squadron then you will get a special gun! granted you have the materials...
            check_AR()
            if check_AR() == True:
                craft_ar()
                choice2 = str(input("> "))
                if choice2 == 'Y':
                    crafting()
                elif choice2 == 'y':
                    crafting()
                elif choice2 == 'N':
                    Next_move()
                elif choice2 == 'n':
                    Next_move()
                elif choice2 == int:
                    error()
                    choice2
                else:
                    error()
                    choice2
            else:
                print("You do not have all of the needed parts")
                crafting()
        elif choice1 == str:
            error()
            choice1
    elif choice == 2:
        reference()
    elif choice == 3:
        print(">>")
        print("You left your workshop")
        Next_move()
    elif choice is str:
        error()
        choice
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
    elif menu_choice is str:
        error()
        menu_choice
    else:
        error()
        Main_Menu()

def end_game(): #A general purpose function to end the game properly.
    sys.exit('"God speed Spiderman"')

#My whole game can be accessed by calling this single function.
Main_Menu()