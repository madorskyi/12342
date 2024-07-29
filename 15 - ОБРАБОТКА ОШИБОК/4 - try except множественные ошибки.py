def get_error_messages(a, b):
    try:
        return a / b

    except ZeroDivisionError:
        return f'{ZeroDivisionError('ZeroDivisionError: Division by zero is not allowed.')}'

    except TypeError:
        return f'{TypeError('TypeError: Unsupported operand type(s)')}'

custom_zero_error = get_error_messages(2, 0)
custom_type_error = get_error_messages(2, 'c')

print(custom_zero_error)
print(custom_type_error)