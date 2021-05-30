fname = input("Give in the file name: ")
fhandle = open(fname, 'r')
count = 0
total = 0.0
average = 0.0
for line in fhandle:
    if line.startswith('X-DSPAM-Confidence:'):
        count = count + 1
        total = total + float(line[19:])
        # print(float(line[19:]))
average = total/count    
print("Average spam confidence:", average)