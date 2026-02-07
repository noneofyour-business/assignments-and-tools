import sys
age = int(input("How old are you? "))

if age<3:
    ticket = 0
    print(f"Your ticket is ${ticket}.")
    sys.exit(age<3)
elif age>=3 and age<=12:
    ticket = 10
    print(f"Your ticket is ${ticket}.")
    sys.exit(age>=3 and age<=12)
elif age>=65:
    ticket = 12
    print(f"Your ticket is ${ticket}.")
    sys.exit(age>=65)

else:
    studentStatus = input("Are you a student? ")
    
if studentStatus == "yes":
    ticket = 15
else:
    ticket = 20

print(f"Your ticket is ${ticket}.")
