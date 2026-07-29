from name_function_example import get_complete_name

def test_first_last_name():
    """Do names like Limp Bizkit work?"""
    complete_name = get_complete_name('limp', 'bizkit')
    assert complete_name == 'Limp Bizkit'

# test files must start with test_ 
# test and one underscore.
# pytest will look for a file that begins with test_
# to run all tests in the file.

# The assertion is claiming that the value of complete_name is 'Limp Bizkit'.

# here's another test function for people who include their middle name:

from name_function_example import get_complete_name

def test_first_last_name():
    """Do names like Limp Bizkit work?"""
    complete_name = get_complete_name('limp', 'bizkit')
    assert complete_name == 'Limp Bizkit'

def test_first_last_middle_name():
    """Do names like Johannes Sebastian Bach pass?"""
    complete_name = get_complete_name(
        'johannes', 'bach', 'sebastian')
    assert complete_name == 'Johannes Sebastian Bach'

# both tests pass!


