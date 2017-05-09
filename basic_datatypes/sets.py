# more methods:
# https://docs.python.org/2/library/stdtypes.html#set-types-set-frozenset

a = set()

print a

a.add(1)

a.add(1)

a.add(2)

print a

a = set([1,2,3]) # create set from a list

print a

print 2 in a

print 10 in a

a.add(10)

print 10 in a

# this will not work
#print a[0]
