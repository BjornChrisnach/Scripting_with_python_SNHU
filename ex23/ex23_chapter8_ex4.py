
result_lst = list()

fhandle = open("romeo.txt", 'r')
lines = fhandle.readlines()

for line in lines:
    words = line.split()
    for word in words:
        if word not in result_lst:
            result_lst.append(word)
        else:
            continue

fhandle.close()
result_lst.sort()
print(result_lst)