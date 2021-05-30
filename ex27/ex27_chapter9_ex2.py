inp = input('Enter a file name: ')
fhandle = open(inp)
count_fri = 1
count_thu = 1
count_sat = 1
dict_email_from_date = dict()
for line in fhandle:
    words = line.split()
    # print('Debug:', words)
    if len(words) == 0 or words[0] != 'From': continue
    # if words[0] != 'From' : continue
    if words[2] == 'Fri':
        dict_email_from_date['Fri'] = count_fri
        count_fri += 1
    elif words[2] == 'Thu':
        dict_email_from_date['Thu'] = count_thu
        count_thu += 1
    elif words[2] == 'Sat':
        dict_email_from_date['Sat'] = count_sat
        count_sat += 1

print(dict_email_from_date)