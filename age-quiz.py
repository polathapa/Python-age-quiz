#Welcome message
print("Welcome to the age commentator!😱")
#User input, saved as an intager variable
age = int(input("What is your age?\n"))
#Variable responses based on user input: conditions : 1.below 13, 2. 21 3.40-64, 4. 65+ 5.100+ 6. 4-20, 22-39.
if age >= 40 and age <= 64:
  print("You're over the hill!")
elif age > 100:
  print("Sorry, you're dead!")
elif age >= 65:
  print("Enjoy your retirement!")
elif age < 13:
  print("You qualify for the kiddie discount.")
elif age == 21:
  print("Congrats on your 21st!")
else:
  print("Age is but a number.")
