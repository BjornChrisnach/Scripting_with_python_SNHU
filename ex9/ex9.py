# "Exercices for chapter 5"
count = 0
while True:
    try:
        number = input("type in a number please: \n")
        if number == "done":
            break
        else:
            number = int(number)
            if count == 0:
                maximum = number
                minimum = number
            else:
                if maximum < number:
                    maximum = number
                if minimum > number:
                    minimum = number
            count = count + 1
    except:
        print("bad data, \nInvalid input")
        continue
print(maximum, minimum)