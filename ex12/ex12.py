# "Exercices for chapter 6"
def count(input_string, search_letter):
    count = 0
    for letter in input_string:
        if search_letter == letter:
            count = count + 1
    print(count)


"These are used for testing purposes in visual studio code or other IDE"
# count("banana", 'a')
# count("apple", 'p')