from stats import get_num_words

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def main():
    path_to_file = "books/frankenstein.txt"
    content = get_book_text(path_to_file)
    num_words = get_num_words(content)
    print(f"Found {num_words} total words")

main()