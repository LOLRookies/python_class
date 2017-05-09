# For string methods, see
# https://docs.python.org/2/library/stdtypes.html#string-methods


s1 = 'Hello, World!'

print s1

print s1[0]

print len(s1)

print s1[len(s1) - 1]

print s1[3:8]

print s1.endswith('!')

print s1.startswith('H')

print s1.startswith('h')

s2 = '  some     spaces   '

print len(s2)

s2 = s2.strip()

print len(s2)
