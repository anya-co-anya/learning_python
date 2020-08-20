# Creating a dictionary.
# Create a function called make_country, which takes in a country’s name and capital as parameters.
# Then create a dictionary from those parameters, with ‘name’ and ‘capital’ as keys.
# Make the function print out the values of the dictionary to make sure that it works as intended.


def make_country(name='country', capital='capital'):
    country_info = {
        'name': name.lower().capitalize(),
        'capital': capital.lower().capitalize()
    }
    for key, value in country_info.items():
        print(f'{key}: {value}')


make_country(name='ukrAine', capital='kyIv')
