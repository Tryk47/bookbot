from stats import *
import sys

def main():
    # Check if the user passed exactly one extra argument (the book path)
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)  # Exit with status code 1 (error)

    filepath = sys.argv[1]
    num_words = get_num_words(filepath)
    string = get_file_content(filepath)
    char_count_dict = char_count(string)
    char_count_sorted_list = list_dict_count(char_count_dict)



    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in char_count_sorted_list:
        print(f"{i["char"]}: {i["num"]}")
    print("============= END ===============")


main()