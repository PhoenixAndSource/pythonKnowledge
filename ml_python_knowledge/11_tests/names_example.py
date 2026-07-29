from name_function_example import get_complete_name

print("Enter 'quit' to quit.")
while True:
    first = input("\nWhat is your first name? ")
    if first == 'quit':
        break
    last = input("What is your last name? ")
    if last == 'quit':
        break

    complete_name = get_complete_name(first, last)
    print(
        f"\tHere is your complete name with appropriate capitalization: {complete_name}."
        )

