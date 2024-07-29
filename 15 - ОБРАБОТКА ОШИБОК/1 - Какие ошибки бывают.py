import builtins

all_builtins = dir(builtins)

for exception in [item for item in all_builtins if isinstance(getattr(builtins, item), type) and issubclass(getattr(builtins, item), BaseException)]:
    print(exception)