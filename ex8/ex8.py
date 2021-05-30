# "Exercices for chapter 5"
count = 0
total = 0
while True:
    try:
        number = input("type in a number please: \n")
        if number == "done":
            break
        else:
            number = int(number)
            count = count + 1
            total = total + number
            average = total / count
    except:
        print("bad data, \nInvalid input")
        continue
print(total, count, average)