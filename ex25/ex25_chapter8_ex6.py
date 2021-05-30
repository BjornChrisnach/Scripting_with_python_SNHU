inp_lst = list()
inp = None

while (True):
        inp = input('Enter a number: ')
        if inp == 'done': break
        inp = int(inp)
        inp_lst.append(inp)
        
max = float(max(inp_lst))
min = float(min(inp_lst))
        
print(f'Maximum: {max}')
print(f'Minimum: {min}')