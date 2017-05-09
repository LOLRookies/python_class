# https://www.tutorialspoint.com/python/python_functions.htm

def printme(str):
   "This prints a passed string into this function"
   print str
   return

# Now you can call printme function
printme("I'm first call to user defined function!")
printme("Again second call to the same function")


def changeme(mylist):
   "This changes a passed list into this function"
   mylist.append([1,2,3,4]);
   print "Values inside the function: ", mylist

# Now you can call changeme function
mylist = [10,20,30];
changeme(mylist);
print "Values outside the function: ", mylist


def changeme(mylist):
   "This changes a passed list into this function"
   mylist = [1,2,3,4]; # This would assig new reference in mylist
   print "Values inside the function: ", mylist

# Now you can call changeme function
mylist = [10,20,30];
changeme( mylist );
print "Values outside the function: ", mylist


total = 0; # This is global variable.
def sum(arg1, arg2):
   # Add both the parameters and return them."
   total = arg1 + arg2; # Here total is local variable.
   print "Inside the function local total : ", total

# Now you can call sum function
sum(10, 20);
print "Outside the function global total : ", total


def printinfo(name, age = 35):
   "This prints a passed info into this function"
   print "Name: ", name
   print "Age: ", age

# Now you can call printinfo function
printinfo(50, 'miki')
printinfo(age=50, name='miki')
printinfo(name='miki')
printinfo('miki')
printinfo(50)
# this will fail
# printinfo(age=50)


def product(a, b):
    return a * b

result = product(10, 15)
print result

def no_return():
    print 'no return function'

result = no_return()
print result

def foo(a, b):
    print a, b
    return

result = foo(10, 15)
print result