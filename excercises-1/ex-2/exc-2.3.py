# Ex3: Write a NumPy program to find the indices of the maximum and minimum values along the given axis of an array
# Input Array [1,6,4,8,9,-4,-2,11]
import numpy as np

Input = [1,6,4,8,9,-4,-2,11]


# cach truyen thong
def find_min_max_element(input:list):
    _sorted_list = input.copy()
    _sorted_list.sort()
    print(_sorted_list)
    return _sorted_list[0], _sorted_list[-1]

print('------Ket qua 1:', find_min_max_element(Input))


# cach 2 dung numpy
def fin_min_max_element_use_np(input: list):
    __array = np.array(input)
    __max_element = np.max(__array)
    __min_element = np.min(__array)
    return __min_element, __max_element

print('------ket qua 2: ', fin_min_max_element_use_np(Input))