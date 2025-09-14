def get_words_count(txt):
    words_list = txt.split()
    return len(words_list)

def get_characters_count(txt):
    letter_map={}
    for letter in txt:
        l=letter.lower()
        if letter_map.get(l):
            letter_map[l]+= 1
        else:
            letter_map[l]= 1

    return letter_map

def get_sorted_list(char_dict):
    new=[]
    for c,q in char_dict.items():
        if not c.isalpha():
            continue
        new.append({"char": c, "num":q})
    return new

def sort_on(item):
    return item["num"]
