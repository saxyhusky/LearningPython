dict1 = {'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'}
print(dict1)
dict1.popitem()
print(dict1)
dict1['fruit'] = 'Mango'
print(dict1)
print(dict1.keys())
print(dict1.values())
print('cake' in dict1)
print('Mango' in dict1.values())

dict2 = {}
for key in dict1.keys():
    dict2[key] = dict1[key].count('t')

print(dict2)

s2= set([0,2,4,6,8,10,12,14,16,18,20])
s3 = set([0,3,6,9,12,15,18])
s4 = set([0,4,8,12,16,20])

print(s2)
print(s3)
print(s4)
print(s3.issubset(s2))
print(s4.issubset(s2))

spython = set(['P','y','t','h','o','n'])
spython.add('i')
fset= frozenset(['m','a','r','a','t','h','o','n'])
print(spython.union(fset))
print(spython.intersection(fset))