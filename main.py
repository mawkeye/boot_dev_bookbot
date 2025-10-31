from stats import get_num_words, get_char_count

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()
        
def main():
    path_to_file = "books/frankenstein.txt"
    content = get_book_text(path_to_file)
    num_words = get_num_words(content)
    print(f"Found {num_words} total words")
    num_chars = get_char_count(content)
    print(num_chars)

main()