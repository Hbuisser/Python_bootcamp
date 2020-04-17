from time import time

def generator(text, sep=" ", option=None):
    lst_check = ["shuffle", "unique", "ordered", None]
    if type(text) is not str or option not in lst_check:
        return "ERROR"
    text_list = text.split(sep)
    text_list2 = []
    if option == "ordered":
        text_list.sort(key=lambda x:(not x.islower(), x))
    elif option == "unique":
        text_list = sorted(set(text_list))
    elif option == "shuffle":
        while len(text_list) > 0:
            text_list2.append(text_list.pop(int(time()) % len(text_list) - 1))
        text_list = text_list2    
    return text_list

text = "Le Lorem Ipsum est simplement du faux texte texte faux."
print(generator(text, sep=" ", option="shuffle"))
