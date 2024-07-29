def get_error_messages(a, b):
    try:
        return a / b

    except ZeroDivisionError:
        return f'{ZeroDivisionError('Error: Division by zero is not allowed.')}'

custom_zero_error = get_error_messages(2, 0)

print(custom_zero_error)