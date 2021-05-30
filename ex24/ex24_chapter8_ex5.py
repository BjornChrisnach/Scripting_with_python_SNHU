fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    words = line.split()
    # print('Debug:', words)
    if len(words) == 0 or words[0] != 'From': continue
    # if words[0] != 'From' : continue
    count += 1
    print(words[1])
print('There were {} lines in the file with From as the first \
word'.format(count))