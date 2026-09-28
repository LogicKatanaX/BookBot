def get_book_text(path):
    with open(path) as f:
        return f.read()


def counts(book_text):
    a = dict()

    for text in book_text:
        char = text.lower()

        if char in a:
            a[char] += 1
        else:
            a[char] = 1

    return a


def sort_on(item):
    return item[1]


def chars_dict_to_sorted_list(num_chars):
    chars = []

    for char in num_chars:
        chars.append((char, num_chars[char]))

    return sorted(chars, key=sort_on, reverse=True)
