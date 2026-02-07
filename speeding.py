speedLimit = int(input("Enter the speed limit (mph). "))
realSpeed = int(input("How fast are you going (mph)? "))
howFar = int(input("How far are you traveling (miles)? "))
limitTime = (howFar/speedLimit)*60
speedingTime = (howFar/realSpeed)*60
timeSaved = limitTime-speedingTime
print("minutes saved", timeSaved)
