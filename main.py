from stats import get_num_words
from stats import get_sorted_list_of_characters
import sys

def get_book_text(path_to_file: str)->str:
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents
def main():
    # path = "./books/frankenstein.txt"
    if len(sys.argv)< 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    content = get_book_text(path)
    num_words = get_num_words(content)
    char_list = get_sorted_list_of_characters(content)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path[2:]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in char_list:
        print(f"{i['char']}: {i['num']}")
    print("============= END ===============")

main()
