#!/usr/bin/python
def square_matrix_simple(matrix=[]):
    response = []
    for i in matrix:
        sub_matrix = map(lambda n: n**2, i)
        response.append(list(sub_matrix))
    return response
