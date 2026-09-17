# short circuit evalutaion
high_income = True
good_credit = True
student = False
if high_income and good_credit and not student:
    print("eligible")

# age should be between 15 and 25
age = 22
if age >= 18 and age < 65:
    print("eligible")

if 18 <= age < 65:
    print("eligible")

# cleaner    = chaining comparision operators
