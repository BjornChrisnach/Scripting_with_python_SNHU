import csv

input_file = open("student_folder/csv/monty_python_movies.csv", "r")
reader = csv.reader(input_file)
for row in reader:
    print(row)