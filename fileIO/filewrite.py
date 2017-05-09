def copy_countries():
    readfp = open('countries', 'r')
    content = readfp.read()
    readfp.close()
    lines = content.split('\n')
    writefp = open('new_countries', 'w')
    for line in lines:
        writefp.write(line)
    writefp.close()

def overwrite():
    writefp = open('new_countries', 'w')
    writefp.write('overwrite content')
    writefp.close()

def append_file():
    writefp = open('new_countries', 'a')
    writefp.write('append content')
    writefp.close()

def write_line():
    lines1 = ['line 1\n', 'line 2\n', 'line 3\n']
    lines2 = ['line 1', 'line 2', 'line 3']
    writefp = open('new_countries', 'w')
    writefp.writelines(lines1)
    writefp.writelines(lines2)
    writefp.close()

copy_countries()
#overwrite()
#append_file()
#write_line()
