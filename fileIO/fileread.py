fp = open('countries', 'r')
content = fp.read()
print content
print 'done reading file'
fp.close()

fp = open('countries', 'r')
idx = 1
for line in fp.readlines():
    print 'line {}: {}'.format(idx, line)
    idx += 1
print 'done reading file'
fp.close()

fp = open('countries', 'r')
idx = 1
for line in fp.readlines():
    print 'line {}: {}'.format(idx, line.strip())
    idx += 1
print 'done reading file'
fp.close()

fp = open('countries', 'r')
while True:
    line  = fp.readline()
    if not line:
        break
    # print repr(line)
    print line
print 'done reading file'
fp.close()

fp = open('countries', 'r')
for line in fp:
    print line
print 'done reading file'
fp.close()

# This is advanced.
with open('countries', 'r') as fp:
    for line in fp:
        print line
