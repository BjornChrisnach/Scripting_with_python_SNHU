# "Exercices for chapter 6"
str = 'X-DSPAM-confidence:0.8475'
pos1 = str.find(':')
num_to_be_float = str[pos1 + 1:]
num_to_be_float = float(num_to_be_float)
# print(num_to_be_float)