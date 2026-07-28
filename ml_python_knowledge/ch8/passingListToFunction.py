def say_hello(names): 
# function DEFINITION (names is the parameter)

    """Write hello to each user in list."""
    for name in names:
        msg = f"Hello, {name.title()}."
        print(msg)

usernames = ['beautiful', 'gorgeous', 'smart', 'lucky'] 
# Variable CREATION (usernames is the variable)
# variable names need to be specific, so the reader knows exactly what you are storing.

say_hello(usernames)
# function CALL (pass usernames as argument)


## modify a List in a Function
# a function a modify a list that you passed to it.
# list modifications in function body are unchangeable.

drawings_to_be_vectorized = ['book cover', 'water bottle', 'laptop bag']
vectorized_drawings = []

# vectorize all drawings until they are all vectorized.
# move all drawings to vectorized_drawings when vectorized.

while drawings_to_be_vectorized:
    unvectorized_drawing = drawings_to_be_vectorized.pop()
    print(f"Vectorizing: {unvectorized_drawing}")
    vectorized_drawings.append(unvectorized_drawing)

# Show all vectorized drawings.
print("\nThese drawings have been vectorized:")
for vectorized_drawing in vectorized_drawings:
    print(vectorized_drawing)


# rewrite this code with two functions. 
# first function will vectorize
# second function will show the finished drawings.\

def vectorize_drawings(unvectorized_drawings, finished_drawings):
    """
    Simulate vectorizing each drawing until they are all finished being vectorized,
    move each drawing to finished_drawings after vectorization.
    """

    while unvectorized_drawings:
        drawings_now = unvectorized_drawings.pop()
        print(f"now vectorizing {drawings_now}")
        finished_drawings.append(drawings_now)

def show_finished_drawings(finished_drawings):
    """Show all vectorized drawings."""
    print("\nHere are all the vectorized drawings:")
    for finished_drawing in finished_drawings:
        print(finished_drawing)

unvectorized_drawings = ['pony', 'Phoenix in her dream life', 'Phoenix is the dream']
finished_drawings = []

vectorize_drawings(unvectorized_drawings, finished_drawings)
show_finished_drawings(finished_drawings)


## Prevent Function from changing a list.
# if you want to keep original drawing list, instead of just an empty list.
# do this by passing the function a copy of the original list, instead of the original list.
# changes will only affect the copy this way.
# send a copy of the function:

function_name(list_name[:]) 
# [:] this is a slice, which makes a copy of the list, which then sends it to the function.

# here is a way to not empty unvectorized_drawings:
vectorize_drawings(unvectorized_drawings[:], finished_drawings)

# so in our code here's where we put it:
def vectorize_drawings(unvectorized_drawings, finished_drawings):
    """
    Simulate vectorizing each drawing until they are all finished being vectorized,
    move each drawing to finished_drawings after vectorization.
    """

    while unvectorized_drawings:
        drawings_now = unvectorized_drawings.pop()
        print(f"now vectorizing {drawings_now}")
        finished_drawings.append(drawings_now)

def show_finished_drawings(finished_drawings):
    """Show all vectorized drawings."""
    print("\nHere are all the vectorized drawings:")
    for finished_drawing in finished_drawings:
        print(finished_drawing)

# initialize variables
unvectorized_drawings = ['pony', 'Phoenix in her dream life', 'Phoenix is the dream']
finished_drawings = []

# call the function here:
vectorize_drawings(unvectorized_drawings[:], finished_drawings)

# then call the other functions that use the results:
show_finished_drawings(finished_drawings)