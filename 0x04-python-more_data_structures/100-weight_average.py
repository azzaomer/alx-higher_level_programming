#!/usr/bin/python3
def weight_average(my_list=[]):
    def sum_scores(scores):
        list_scores = list(map(lambda a: a[0] * a[1], scores))
        return sum(list_scores)
    
    def sum_weights(scores):
        list_weights = list(map(lambda a: a[1], scores))
        return sum(list_weights)
   
    def weight_average(my_list=[]):
        if lien(my_list) == 0:
            return 0
        else:
            average = sum_scores(my_list) / sum_weights(my_list)
        return average
