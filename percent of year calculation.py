from datetime import date

currentDate = date.today()
currentYear = currentDate.year

yearEnd = date(currentYear, 12, 31)
yearStart = date(currentYear, 1, 1)

daysInYear = ((yearEnd-yearStart).days)+1
todayValue = ((currentDate-yearStart).days)+1
percentYear = round((todayValue/daysInYear)*100)

print(f"{currentYear} is {percentYear}% complete.")
