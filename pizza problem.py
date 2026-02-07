#Step One: How many slices will each person eat?
person1= int(input("How many slices will person one eat?"))
person2= int(input("How many slices will person two eat?"))
person3= int(input("How many slices will person three eat?"))
person4= int(input("How many slices will person four eat?"))

#Step Two: How many pizzas will we need and how many slices will be left?
import math
slices_needed=person1+person2+person3+person4
pizzas_needed=math.ceil(slices_needed/8)
slices_left=(pizzas_needed*8)-slices_needed

#Step Three: Answer.
if pizzas_needed==1 and slices_left==1:
    print(f"You need to buy {pizzas_needed} pizza and will have {slices_left} slice left over.")
if (pizzas_needed>1 or pizzas_needed==0) and slices_left==1:
    print(f"You need to buy {pizzas_needed} pizzas and will have {slices_left} slice left over.")
if pizzas_needed==1 and (slices_left>1 or slices_left==0):
    print(f"You need to buy {pizzas_needed} pizza and will have {slices_left} slices left over.")
if (pizzas_needed>1 or pizzas_needed==0) and (slices_left>1 or slices_left==0):
    print(f"You need to buy {pizzas_needed} pizzas and will have {slices_left} slices left over.")
