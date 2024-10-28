# print("Hello"[0])
# print("Hello"[4])

# print(len("12345"))

# print(type(True))

# number = int("1234")
# print(type(number))

# print("Number of letters in your name : " + str(len(input("Enter your name \n"))))

# print(10 + 25)
# print(1 - 5)
# print(1 * 6)
# print(5 / 3)
# print(5 // 3)
# print(2 ** 4)

# Bmi Calculator

# height = 1.65
# weight = 84
# bmi = weight / height ** 2
# print(round(bmi, 2))
# print(f"Your score is {round(bmi, 2)}")

print("Welcome to the tip calculator!")
bill = input("What was the total bill? $ ")
tip_percentage = input("How much tip would you like to give? 10, 12, or 15 ? ")
no_of_people = input("How many people to split the bill? ")
tip_amount = float(bill) * float(tip_percentage) / 100
payable_amount_per_person = (float(bill) + tip_amount) / int(no_of_people)
print(f"Each person should pay : ${round(payable_amount_per_person, 2)}")