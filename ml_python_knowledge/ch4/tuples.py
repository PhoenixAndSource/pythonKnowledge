## Tuples

# A tuple is like a list, but cannot be changed. Python calls this immutable.
# Tuples use parantheses, and commas.
# lists use square brackets.
# Lists you can change.

# example of use for tuple: dimensions of a rectangle that you don't want to change.

rectangleMeasurements = (100, 50)
print(rectangleMeasurements[0])
print(rectangleMeasurements[1])

# we cannot change the value of the first dimension.

# to show it is a tuple when we only have one element, we can add a comma.

my_tuple = (5,)

# usually we don't make tuples with just one element, but it can happen when tuples are made automatically.

## Loop through all values in a tuple

rectangleMeasurements = (100, 50)
for newMeasurements in rectangleMeasurements:
    print(newMeasurements)

## Assign new value to an element in a tuple
# example: change dimensions of the rectangle:

rectangleMeasurements = (100, 50)
print("Original dimensions:")
for newMeasurements in rectangleMeasurements:
    print(newMeasurements)

# reassign the variable to a new tuple with the new measurements.

rectangleMeasurements = (400, 200)
print("\nNew dimensions:")
for newMeasurements in rectangleMeasurements:
    print(newMeasurements)
