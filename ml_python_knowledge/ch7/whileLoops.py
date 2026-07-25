#while loop counts from 2-4:

now_number = 2
while now_number <= 4:
    print(now_number)
    now_number += 1

# allowing the user choose when you quit

prompt = "\nI will confirm what you say here:"
prompt += "\nWrite 'quit' to stop the program. "

message = ""
while message != 'quit': # prints quit like it's a message, so we'll fix it in the next code.
    message = input(prompt)
    print(message)

prompt = "\nWhat does your fortune say? I will read your fortune back to you."
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
    message = input(prompt)

    if message != 'quit': # this code checks before writing the message and prints out the message only if it doesn't match the value quit:
        print(message)

## A flag

prompt = "\nI will repeat your magic mantra with you:"
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)

## Exit a Loop using break
# control which lines of code python should read and which to skip, whenever you wish it to use the code.

prompt = "\nTell me your favorite place in your memory:"
prompt += "\n(Write 'done' when you are done. )"

while True:
    beautifulMemory = input(prompt)

    if beautifulMemory == 'done':
        break
    else:
        print(f"Let's visit {beautifulMemory.title()}!")

## Use continue statement to go back to the beginning of the loop based on a conditional test.

current_age = 0
while current_age < 10:
    current_age += 1
    if current_age % 2 == 0:
        continue
    
    print(current_age)

## avoid infinite loops

# this code counts from 1 to 15
x = 1
while x <= 15:
    print(x)
    x += 1

# if x += 1 is not present, the loop will go on forever.
# x = 1
# while x <= 5:
#    print(x)



