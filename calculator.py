print('Simple calculator!')

first_value = input('First number? ')

if first_value.isnumeric() == False :
    print('Please input a number.')
    exit()

first_value = int(first_value)

operation = input ('Operation? ')


second_value = input('Second number? ')

if second_value.isnumeric() == False:
    print('Please input a number.')
    exit()

second_value = int(second_value)

if operation == '+':
    sum = first_value + second_value
    print('Sum: ' + str(sum))
elif operation == '-':
    difference = first_value - second_value
    print('Difference: ' + str(difference))
elif operation == '/':
    quotient = first_value / second_value
    print('Quotient: ' + str(quotient))
elif operation == '*':
    product = first_value * second_value
    print('Product: ' + str(product))
elif operation == '**':
    exponent = first_value ** second_value
    print('Exponent: ' + str(exponent))
elif operation == '%':
    modulus = first_value % second_value
    print('Modulus: ' + str(modulus))
else:
    print('Operation not recognize.')
    exit()
