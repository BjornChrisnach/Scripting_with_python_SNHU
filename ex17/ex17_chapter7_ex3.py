fname = input("Enter the file name: ")
count = 0
if fname == "na na boo boo":
    print("NA NA BOO TO YOU - You have been punk'd!")
else:
    fhandle = open(fname, 'r')
    for line in fhandle:
        if line.startswith('Subject:'):
            count = count + 1
    print("There were", count, f"subject lines in {fname}")