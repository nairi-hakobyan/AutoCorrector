import re

def get_words(path='book.txt'):
    with open(path, 'r') as f:
        file_name_data = f.read()
        file_name_data=file_name_data.lower()
        words = re.findall('\w+',file_name_data)
    # This is our vocabulary
    V = set(words)
    print("Top ten words in the text are:", words[0:10])
    print("Total Unique words are.", len(V))
    return words
