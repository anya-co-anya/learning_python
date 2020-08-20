input_string = 'Such a perfect code'
output_string = None

if len(input_string) >= 2:
    output_string = input_string[:2] + input_string[-2:]
else:
    output_string = ''

print(output_string)

