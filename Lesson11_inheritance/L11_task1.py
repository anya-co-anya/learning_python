# School

# Make a class structure in python representing people at school.
# Make a base class called Person, a class called Student, and another one called Teacher.
# Try to find as many methods and attributes as you can which belong to different classes, and keep in mind which are common and which are not.
# For example, the name should be a Person attribute, while salary should only be available to the teacher.

class Person:
    def __init__(self, first_name='noname', second_name='noname', age=0):
        self.first_name = first_name
        self.second_name = second_name
        self.age = age
        self.__is_hungry = True

    def talk(self):
        print(f'Hi, I`m {self.first_name} {self.second_name}.')

    def eat(self):
        self.__is_hungry = False


class Teacher(Person):
    def __init__(self, first_name='noname', second_name='noname',  age=0, salary=0, is_tutor=False):
        super().__init__(first_name, second_name, age)
        self.__salary = salary
        self.__is_tutor = is_tutor

    def talk(self):
        super().talk()
        print('Go to your class!')

    def get_promotion(self, amount=0):
        self.__salary += amount

    def make_tutor(self):
        self.__is_tutor = True


class Student(Person):
    def __init__(self, first_name='noname', second_name='noname', age=0, grade=60):
        super().__init__(first_name, second_name, age)
        self.__grade = grade

    def get_good_mark(self):  # to change average grade
        if self.__grade <= 100:
            self.__grade = self.__grade * 1.1
            print(self.__grade)

    def get_bad_mark(self):
        if self.__grade > 0:
            self.__grade = self.__grade * 0.9


if __name__ == '__main__':
    student1 = Student('Maks', 'Maksovich', 18, 30)
    teacher = Teacher('Olga', 'Oliivna', 56, 1000, False)

    student1.talk()
    teacher.talk()
    student1.get_good_mark()




