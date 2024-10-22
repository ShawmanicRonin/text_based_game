thing = input()
if thing == 'bob':
    x = thing
    print(x)
else:
    #print('not ' + x)#x is not defined because scoping allows x to only be defined in the if statement. 



 def doThing():
    x = 24
    print(x)

x = 'bob'
doThing()
print(x)#This will print 24 and bob because as soon as doThing finishes, it dies


y = 'ashley'

def doThing(thing):
    return thing +1

y = doThing(24)
print(y)#This will print 25 because 24 has been put into the function



def doThing(y):
    y[0] = 4

y = [1, 2, 3]
doThing(y)
print(y)#This will print 4, 2, 3 because the function has modified the 0 index in y list because '0' is a location in memory which means any changes made by the function are saved to memory. Use lists instead of variables.

def doThing(choice):
    if choice == 'a':
        return 4, 32
    elif choice == 'b':
        return 'Hello'
    

for i in range(5):
    x = i
print(x)