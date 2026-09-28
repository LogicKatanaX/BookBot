import sys
from stats import get_book_text,counts,chars_dict_to_sorted_list
def print_report(book_path, word_count, sorted_chars):
    # Header
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")

    # Word count
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")

    # Character count
    print("--------- Character Count -------")

    for char, count in sorted_chars:
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    book_text = get_book_text(book_path)
    words = book_text.split()

    char_counts = counts(book_text)
    sorted_chars = chars_dict_to_sorted_list(char_counts)

    print_report(book_path, len(words), sorted_chars)

main()




