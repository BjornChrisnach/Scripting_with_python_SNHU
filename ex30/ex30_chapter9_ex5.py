inp = input('Enter a file name: ')
fhandle = open(inp)
email_lst = list()
i = 0
j = 0
dict_email_from_date = dict()

for line in fhandle:
    words = line.split()
    # print('Debug:', words)
    if len(words) == 0 or words[0] != 'From': continue
    # if words[0] != 'From' :

    # fill up the email lst, with domain names
    split_lst = list()
    split_lst = words[1].rsplit('@')
    split_sentence = split_lst[1]
    email_lst.append(split_sentence)
    # set the range max to a variable
    length = len(email_lst) - 1
    # if minimum length = 2, compare them if True set the value j as the count
    if len(email_lst) >= 2:
        for k in range(0, length):
            if email_lst[k] == email_lst[length]:
                # retrieve the current count, add one
                j = dict_email_from_date[email_lst[i]]
                j += 1
                dict_email_from_date[email_lst[i]] = j
                break
            # add as a new dictioanary item
            elif k == length or k == length - 1:
                j = 1
                dict_email_from_date[email_lst[i]] = j
                break
            else:
                continue
    
    # if length != 2, then it's 1, so add as a new dictionary item
    else:
        j = 1
        dict_email_from_date[email_lst[i]] = j

    i += 1

# Done, print the result 
print(dict_email_from_date)

# maximum = (max(dict_email_from_date.values()))
# maximum_key = dict_email_from_date.keys()
# for key in maximum_key:
#     if dict_email_from_date[key] == maximum:
#         maximum_key = key
# print(maximum_key, maximum)