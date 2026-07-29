from pathlib import Path

def count_words(path):
    """Count the words in a file."""
    try: 
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Sorry, the file {path} does not exist.")

    # sometimes you want the program to fail silently:
    except FileNotFoundError:
        pass # it's a placeholder, reminder that you're not doing anything specific, thatyou'll address later.
    
    else:
        # Count the number of words in file:
        words = contents.split()
        num_words = len(words)
        print(f"the file {path} has about {num_words} words.")
        # path = Path('the_giving_tree.txt')
        # count_words(path)

filenames = ['the_giving_tree.txt', 'falling_up.txt', 'the_voice.txt']
for filename in filenames:
    path = Path(filename)
    count_words(path)

