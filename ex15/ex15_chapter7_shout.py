fname = input('Give the file to open: ')
try:
    fhand = open(fname)
    for line in fhand:
        print(line.upper())
except:
    print('give in a correct file name.')