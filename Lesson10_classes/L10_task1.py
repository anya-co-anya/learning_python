# A Person class

# Make a class called Person.
# Make the __init__() method take firstname, lastname, and age as parameters and add them as attributes.
# Make another method called talk() which makes prints a greeting from the person containing, for example like this:
# “Hello, my name is Carl Johnson and I’m 26 years old”.

class Person:
    def __init__(self, firstname='noname', lastname='noname', age=15):
        self.firstname = firstname.lower().capitalize()
        self.lastname = lastname.lower().capitalize()
        self.age = age

    def talk(self):
        print(f'Hello, myname is {self.firstname} {self.lastname} and I`m {self.age} years old')


if __name__ == '__main__':
    katya = Person("kate", 'puzikOva', 32)
    katya.talk()