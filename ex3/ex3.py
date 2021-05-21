"Second project of the edx course"
hours = float(input("Type in your work hours :"))
rate = float(input("Type in your hourly rate :"))
pay = hours * rate
pay = round(pay, 2)
print(f"your pay is {pay}")