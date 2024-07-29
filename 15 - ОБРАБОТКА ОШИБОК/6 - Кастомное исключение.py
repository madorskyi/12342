class MyError(Exception):
    """A custom exception class"""

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f"MyError: {self.message}"

    def log_error(self):
        # Example method to log the error
        print(f"Logging error: {self.message}")

    def handle_error(self):
        # Example method to handle the error
        print(f"Handling error: {self.message}")

def get_error_messages():
    raise MyError("This is a custom exception")


custom_zero_error = get_error_messages()

print(custom_zero_error)