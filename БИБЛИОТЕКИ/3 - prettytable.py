from prettytable import PrettyTable
import builtins

functions_list = dir(builtins)
pretty_table = PrettyTable()
pretty_table.field_names = ["Built-in Functions"]

for function in functions_list:
    if "__" not in function:  # exclude function names with __
        if function[0].islower():
            pretty_table.add_row([function])

print(pretty_table)