def get_error_messages(a, b):
    try:
        print(a / b)

    except ZeroDivisionError:
        print('Error: Division by zero is not allowed.')

    else:
        print('No errors occurred.')

    finally:
        print('Finally block executed.')



get_error_messages(2, 0)