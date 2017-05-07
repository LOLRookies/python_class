class Person:
    # Notice self must be put first
    def __init__(self, name, age, gender):
        self.name = name
        self.__age = age
        self.gender = gender



def main():
    p1 = Person('xiaoming', 20, 'm')
    p2 = Person('xiaohong', 19, 'f')

    print p1.name
    print p2.name

    print p1.age
    print p1.age

if __name__ == "__main__":
    main()