# Doggy age
#
# Create a class Dog with class attribute `age_factor` equals to 7.
# Make __init__() which takes values for a dog’s age.
# Then create a method `human_age` which returns the dog’s age in human equivalent.

class Dog:
    age_factor = 7

    def __init__(self, age=5):
        self.age = age

    def human_age(self):
        return self.age*self.age_factor


if __name__ == '__main__':
    barsik = Dog(8)
    print(f'If it was a human, barsik would be {barsik.human_age()} years old. But he is just {barsik.age}.')
