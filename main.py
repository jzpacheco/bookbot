import sys

from stats import get_characters_count, get_sorted_list, get_words_count


def get_book_text(file_path):
    with open(file_path) as file:
        txt=file.read()

    return txt

if __name__ == '__main__':
    if len(sys.argv) <2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)

    file_path=sys.argv[1]
    txt=get_book_text(file_path)
    characters=get_characters_count(txt)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {get_words_count(txt)} total words")
    print("--------- Character Count -------")
    for i in get_sorted_list(characters):
        print(f"{i.get("char")}: {i.get("num")}")

