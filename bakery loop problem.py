#define number of items
import sys
muffins = 10
cupcakes = 10

print("This bakery sells muffins and cupcakes.")

#write a loop asking the user what item they want to buy
while muffins>0 and cupcakes>0:
    item = input("Would you like to buy an item?")
    if item == "yes":
        item = input("muffin or cupcake?")
    if item == "muffin":
        muffins = muffins-1
    if item == "cupcake":
        cupcakes = cupcakes-1
    if item == "no":
        if muffins!=1 and cupcakes!=1:
            print(f"There are {muffins} muffins left and {cupcakes} cupcakes left.")
        if muffins!=1 and cupcakes==1:
            print(f"There are {muffins} muffins left and {cupcakes} cupcake left.")
        if muffins==1 and cupcakes!=1:
            print(f"There is {muffins} muffin left and {cupcakes} cupcakes left.")
        if muffins==1 and cupcakes==1:
            print(f"There is {muffins} muffin left and {cupcakes} cupcake left.")
        sys.exit(item == "no")

#tell the user when they buy all of an item
if muffins==0 and cupcakes>0:
    print("The bakery is out of muffins.")
    while muffins == 0 and cupcakes>0:
        outOfMuffins = input("Would you like to buy a cupcake?")
        if outOfMuffins == "yes" or "cupcake":
            cupcakes = cupcakes-1
        if outOfMuffins == "no":
            if cupcakes==1:
                print(f"There are no muffins and 1 cupcake left.")
                sys.exit(cupcakes==1)
            if cupcakes>1:
                print(f"There are no muffins and {cupcakes} cupcakes left.")
                sys.exit(cupcakes>1)
            
if cupcakes==0 and muffins>0:
    print("The bakery is out of cupcakes.")        
    while cupcakes == 0 and muffins>0:
        outOfCupcakes = input("Would you like to buy a muffin?")
        if outOfCupcakes == "yes" or "muffin":
            muffins = muffins-1
        if outOfCupcakes == "no":
            if muffins==1:
                print(f"There are no cupcakes and 1 muffin left.")
                sys.exit(muffins==1)
            if muffins>1:
                print(f"There are no cupcakes and {muffins} muffins left.")
                sys.exit(muffins>1)

#congratulate the user if they buy all the items
if muffins==0 and cupcakes==0:
    print("Thank you for buying all of our bakery's items!")
    

