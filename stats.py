# inputs a text file and returns the contents as a string.
def get_file_content(filepath):
    with open(filepath) as file:
        return file.read()

# inputs a book in a text file and returns the number of words
def get_num_words(filepath):
    book = get_file_content(filepath)
    word_list = book.split()
    word_count = len(word_list)
    return word_count

# inputs text as a string and returns a dict with charactor counts.
def char_count(string):
    char_dict = {}
    for char in string:
        char = char.lower()
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(dict):
    return dict["num"]

# Inputs a dict of letters with their count, returns a list with a dict for each letter and their count. 
# e.g. {"char": "b", "num": 4868}
def list_dict_count(dict):
    list_dict = []

    for key in dict:
        if key.isalpha():
            list_dict.append({"char": key, "num": dict[key]})
    
    list_dict.sort(reverse=True, key=sort_on)

    return list_dict

