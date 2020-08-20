# Mathematician
#
# Implement a class Mathematician which is a helper class for doing math operations on lists
# The class doesn't take any attributes and only has methods:
# square_nums (takes a list of integers and returns the list of squares)
# remove_positives (takes a list of integers and returns it without positive numbers
# filter_leaps (takes a list of dates (integers) and removes those that are not 'leap years'

class Mathematician:
    def square_nums(self, integers=[]):
        calculated_integers = [i**2 for i in integers]
        return calculated_integers

    def remove_positives(self, integers=[]):
        calculated_integers = [i for i in integers if i <= 0]
        return calculated_integers

    def filter_leaps(self, years=[]):
        leap_years = []
        for year in years:
            if year % 4 == 0:
                if year % 100 == 0 and year % 400 != 0:
                    continue
                else:
                    leap_years.append(year)
        return leap_years


if __name__ == '__main__':
    m = Mathematician()
    print(m.square_nums([7, 11, 5, 4]))
    print(m.remove_positives([26, -11, -8, 13, -90]))
    print(m.filter_leaps([2001, 1884, 1995, 2003, 2020, 1800]))




