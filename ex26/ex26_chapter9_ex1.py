j = 0
word_lst = list()
words_dict = dict()

fhandle = open('words2.txt', 'r')
# split up into words
for line in fhandle:
    words = line.split()
    # fill up the word_lst
    for word in words:
        word_lst.append(word)
    # Check for double words
    for word in words:
        for i in range(len(word_lst)-1):
            # if for some reason i would go out of index, don't let them
            if i > (len(word_lst) - 1):
                i = 0
                continue
            # use the reset of i to 0,  to reset j to 0 also
            if i == 0:
                j = 0
            # if it's a first equal, just set j to +1
            if word == word_lst[i]:
                j += 1
                # print(word_lst[i])
                # if it's a second equality, remove the word, one time, from the list
                if j > 1:
                    word_lst.remove(word)
# fill in the dictionary keys
for word in word_lst:
    words_dict[word] = None
    # print(words_dict)

# used for testing purposes with visual studio code or other IDE
# print('programs' in words_dict.keys())
# print('could' in words_dict.keys())