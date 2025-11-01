def get_num_words(book_text: str)->int:
    word_list = book_text.split()
    return len(word_list)

def get_character_amounts(book_text: str)->dict[chr, int]:
    characters = {}
    book_text = book_text.lower()
    for i in book_text:
        characters[i] = characters.get(i, 0) + 1
    return characters

def sort_on(items):
    return items['num']

def get_sorted_list_of_characters(book_text: str):
    chars = get_character_amounts(book_text)
    char_list = []
    for i in chars.keys():
        if i.isalpha():
            char_list.append({'char': i , 'num':chars[i]})
    char_list.sort(reverse = True, key=sort_on)
    return char_list


