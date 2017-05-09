nums = [1,3,4,5,6]

for num in nums:
    print num


numset = set()
numset.add(30)
numset.add(30)
numset.add(10)
numset.add(20)

for element in numset:
    print element

numset.remove(20)
for element in numset:
    print element


idx = 0
while idx < 10:
    print idx,
    idx += 1
print
print

d = {'country':'USA', 'state':'ny', 'city':'nyc', 'population':8000000}
for key in d.keys():
    print key, d[key]
print

for key in d:
    print key, d[key]
print

print d.items()

for key, value in d.items():
    print key, value

