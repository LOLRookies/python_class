class Person:

    def __init__(self, name, age,ssn):
        # public variable
        self.name = name
        # private variable, cannot be accessed outside
        self.__age = age
        self.__ssn = ssn

    def get_age(self):
        return self.__age



def main():
    xiaoming = Person('xiaoming', 19,ssn)
    print xiaoming.name
    # print xiaoming.__age


    print xiaoming.__ssn
    
if __name__ == "__main__":
    main()