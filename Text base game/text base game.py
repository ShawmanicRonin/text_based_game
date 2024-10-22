import random

parts = ['stock', 'barrel', 'trigger', 'sights', 'reciever',] #inventory items are based on basic gun parts
craftables = ['rifle', 'handgun', 'shotgun'] #craftable items
inventory = []
stock = 'stock'
barrel = 'barrel'
trigger = 'trigger'
sights = 'sights'
reciever = 'reciever'
rifle = 'rifle'
handgun = 'handgun'
shotgun = 'shotgun'

def collect(part):
    inventory.append(result)

def search():#I need help making sure this is a good way to perform the search. Search is my mine function
    search = int(input('How many builddings will you search?'))
    while search > 0:
        return random.randint(1, 100)
        result = random.randint(1, 100)
        search -= 1#right now it is not keeping track of how many buildings you input

def craft():
    print('What would you like to craft?')
    

result = search()
if result <= 39:
    collect(stock) #I am calling the give function collect
elif result <= 69:
    collect(barrel)
elif result <= 89:
    collect(trigger)
elif result <= 97:
    collect(sights)
else:
    collect(reciever)
print(result) #this will need to be changed to return instead of print after testing