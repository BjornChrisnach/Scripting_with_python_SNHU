eng2sp = dict()

eng2sp['one'] = 'uno'
print(eng2sp)
eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
print(eng2sp)
print(eng2sp['two'])
print(len(eng2sp))

print('one' in eng2sp)
print('uno' in eng2sp)

vals = list(eng2sp.values())
print('uno' in vals)

