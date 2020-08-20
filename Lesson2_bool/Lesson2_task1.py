name = 'Anna'
day = 'Monday'
greeting = 'Good day {}! {} is a perfect day to learn some python.'

print(f'Good day {name}! {day} is a perfect day to learn some python.')
print('Good day %s! %s is a perfect day to learn some python.' % (name, day))
print(greeting.format(name, day))