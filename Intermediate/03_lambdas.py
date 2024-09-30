#Lambdas

#Son funciones anonimas 

sum_two_values = lambda first_value, second_value: first_value * second_value
print(sum_two_values(5, 7))

multiply_two_values = lambda first_value, second_value: first_value * second_value -3
print(multiply_two_values(5, 7))

def sum_three_values(value):
    return lambda first_value, second_value: first_value + second_value + value

print(sum_three_values(5)(2, 4))
