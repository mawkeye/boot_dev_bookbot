import sys
from stats import get_num_words, get_char_count, get_sorted_list

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()
        
def main():    
    path_to_file = ""
    try:
        path_to_file = sys.argv[1]   
    except IndexError:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    content = get_book_text(path_to_file)
    num_words = get_num_words(content)
    num_chars = get_char_count(content)
    sorted_list = get_sorted_list(num_chars)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for items in sorted_list:
        if(items["char"].isalpha()):
            print(f"{items["char"]}: {items["num"]}")
    print("============= END ===============")
    

main()