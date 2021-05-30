# "Exercices chapter 3"
hours = float(input("Type in your work hours : \n"))
rate = float(input("Type in your hourly rate : \n"))
if hours < 40:
    pay = hours * rate
else:
    bonus_rate = float((rate * 1.5))
    pay = (40.0 * rate) + ((hours - 40.0) * bonus_rate)

pay = round((pay), 2)
print(f"your pay is {pay}")