class Person(object):
    # Class variable
    planet = 'earth'

    def __init__(self, name):
        self.name = name


def main():
    xiaoming = Person('xiaoming')
    xiaohong = Person('xiaohong')
    print xiaoming.name
    print xiaohong.name


    print Person.planet
    print xiaoming.planet
    print xiaohong.planet


    # class variable and instance variable are not the same thing
    xiaoming.planet = 'mars'
    print xiaoming.planet
    print xiaohong.planet


    # class variable and instance variable are not the same thing
    del xiaoming.planet
    print xiaoming.planet

if __name__ == "__main__":
    main()