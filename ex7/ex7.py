# "Exercices chapter 3"
try:
    grade = float(input("give in ascore between 0.0 and 1.0: \n"))
    if grade > 1.0:
        print("Bad score")
    elif grade >= 0.9:
        print("A")
    elif grade >= 0.8:
        print("B")
    elif(grade >= 0.7):
        print("C")
    elif(grade >= 0.6):
        print("D")
    elif(grade < 0.6 and grade >= 0.0):
        print("F")
    elif(grade < 0.0):
        print("Bad score")
except:
    "Bad score"