#import libraries and functions
from datetime import date, datetime, timedelta
import math

#how much money
goal = float(input("How much money is your goal? $"))
goalComplete = float(input("How much money have you already put toward this goal? $"))
goalLeft = goal - goalComplete
averagePaycheck = float(input("How much of your average paycheck can you put toward this goal? $"))

#define dates
print("When is your nearest paycheck?")
firstPay = input("YYYY-MM-DD ")
firstPayCalc = datetime.strptime(firstPay, "%Y-%m-%d")

#calculate
paychecksNeeded = math.ceil(goalLeft/averagePaycheck)-1
finishDate = (firstPayCalc + timedelta(days=(paychecksNeeded*14))).date()

#tell the user
print(f"It will take you until {finishDate} to meet your goal.")

