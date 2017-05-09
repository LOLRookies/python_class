# more methods:
# https://docs.python.org/2/library/stdtypes.html#mapping-types-dict

a = dict()

print a

a['one'] = 1

print a

a['two'] = 2

print a

a['one'] = 'one'

print a

print a['one']

print a['two']

# this will not work
#print a['three']

print a.get('three') # None since 'three' is not a key

del a['two']

print a

a = {'name':'John', 'age': 20, 'student': True}

print a

