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

def sort_on(items):
    return items["num"]

def get_sorted_list(dict_to_sort):
    sorted_list = []    
    for char in dict_to_sort:
        num = dict_to_sort[char]
        sorted_list.append({"char":char, "num":num})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list