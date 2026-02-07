#Step 1: Prompt and User Input
print("Assume there are only men and women in the class. Enter the number of men and the number of students.")

men = int(input("Enter the number of men in the class."))
students = int(input("Enter the number of students in the class."))

#Step 2: Calculate using values
women = students-men
mpercent = round((men/students)*100)
wpercent = round((women/students)*100)

#Step 3: Answer
print(f"The class is {mpercent}% men and {wpercent}% women.")
