def best_score(a_dictionary):
    if bool(a_dictionary) == False:
        return ('None')
    else:
        Key_max = max(a_dictionary, key = lambda x: a_dictionary[x])
        return (Key_max)
       
