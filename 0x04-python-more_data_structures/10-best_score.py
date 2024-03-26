def best_score(a_dictionary):
    if a_dictionary:
        Key_max = max(a_dictionary, key=a_dictionary.get)
        return (Key_max)
    else:
        return None
       
