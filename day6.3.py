high_income = False
good_credit = True
if high_income and good_credit:
    print("Eligible")
else:
    print("not eligible")

high_income = False
good_credit = True
if high_income or good_credit:
    print("Eligible")
else:
    print("not eligible")

high_income = False
good_credit = True
student = True
if not student:
    print("Eligible")
else:
    print("not eligible")

high_income = False
good_credit = True
student = True
if (high_income or good_credit) and not student:
    print("eligble")
else:
    print("N.E")

age = 20
if age >= 18:
    print("adult")
else:
    print("minor")
