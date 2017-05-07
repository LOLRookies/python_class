# base class
# algorithm + data structure

class Person(object):

    def __init__(self, name, age):
        self.name = name
        # private data, cannot be accessed outside
        self.__age = age

    def get_age(self):
        return self.__age



class Student(Person):
    def __init__(self, name, age, school, score):
        super(Student, self).__init__(name, age)
        self.school = school
        self.score = score



xiaoming = Student('xiaoming', 20, 'nyu', 100)
print xiaoming.name
print xiaoming.get_age()


p = Person('xiaohong', 20)
s = Student('xiaoming', 20, 'nyu', 100)

# p is a person, p is not a student
# s is a person, s is a student
isinstance(p, Student)

# practise: define teacher class. (name, age, school, course)