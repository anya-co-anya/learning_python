# validate email - users, admins

class Human:
    mail_pref = ''

    def __init__(self, email):
        if self.__class__.is_valid_email(email):
            self.email = email
        else:
            self.email = 'booo'


    @classmethod
    def is_valid_email(cls, email: str) -> bool:
        return email.startswith(cls.mail_pref)

    def _privet(self):
        print('hi from human')


class User(Human):
    mail_pref = 'user_'


class Admin(Human):
    mail_pref = 'admin_'

    def privet2(self):
        return self._privet()

# Farm

class Farmer:

    def __init__(self):
        self.__animals = []

    def add_animal(self, animal):
        if isinstance(animal, Animal):
            self.__animals.append(animal)

    def display_usability(self):
        for animal in self.__animals:
            print(animal.usability)
        if not self.__animals:
            print('No animals')

    def sell_animal(self, animal, buyer):
        if animal in self.__animals:
            self.__animals.pop(self.__animals.index(animal))
            animal.owner = buyer
        else:
            print(f'cannot sell {animal}')


class Animal:
    def __init__(self, price, owner: Farmer):
        self.price = price
        self.owner = owner

    def __str__(self):
        return self.__class__.__name__

    @property
    def usability(self):
        return f'Can be sold on {self.price}'

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, new_owner):
        if isinstance(new_owner, Farmer):
            self.__owner = new_owner
            new_owner.add_animal(self)
        else:
            print('Wrong type')


class Chicken(Animal):

    @property
    def usability(self):
        return super().usability + f' and make some eggs'


class Cow(Animal):
    @property
    def usability(self):
        return super().usability + f' and make some milk'


if __name__ == '__main__':
    # oleh = User('user_ol@gmail.com')
    # print(oleh.email)
    # oleh2 = Admin('admin_dfvdf@dfv')
    # print(oleh2.email)
    # oleh2.privet2()


    maks = Farmer()
    mark = Farmer()
    koko = Chicken(9, maks)
    burka = Cow(8, maks)

    print('Maks:')
    maks.display_usability()
    print('Mark:')
    mark.display_usability()

    maks.sell_animal(koko, mark)
    maks.sell_animal(koko, mark)
    print('after selling')
    print('Maks:')
    maks.display_usability()
    print('Mark:')
    mark.display_usability()