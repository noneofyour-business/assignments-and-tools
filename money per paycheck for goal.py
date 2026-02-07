#import libraries and functions
from datetime import datetime

#how much money
goal = float(input("How much money is your goal? $"))
goalComplete = float(input("How much money have you already put toward this goal? $"))
goalLeft = goal - goalComplete

#define dates
print("When do you want this goal met?")
dueDate = input("YYYY-MM-DD ")
dueDateCalc = datetime.strptime(dueDate, "%Y-%m-%d")

print("When is your nearest paycheck?")
firstPay = input("YYYY-MM-DD ")
firstPayCalc = datetime.strptime(firstPay, "%Y-%m-%d")

#calculate
timeToPay = dueDateCalc - firstPayCalc
payPeriods = int((timeToPay.days/14)+1)
moneyPerPaycheck = round((goalLeft/payPeriods),2)

#tell the user
print(f"You have {payPeriods} paychecks to meet your goal, and you will need ${moneyPerPaycheck} each paycheck to meet your goal by the due date.")
