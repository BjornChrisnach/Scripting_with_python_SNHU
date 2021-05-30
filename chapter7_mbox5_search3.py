fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    # skip 'uninteresting lines'
    if not line.startswith('From:'):
        continue
    # process our 'interesting' line
    print(line)