def get_num_words(text):
    return len(text.split())

def get_char_count(text):
    char_dict = {}
    search_text = text.lower()
    for c in search_text:
        if (c in char_dict):
            char_dict[c] += 1
        else:
            char_dict[c] = 1
    return char_dict
	
