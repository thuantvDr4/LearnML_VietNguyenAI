
# Ex2: Write a NumPy program to test whether each element of a 1-D array is also present in a second array
# Input Array1: [ 0 10 20 40 60]
#       Array2: [10, 30, 40]

import numpy as np

# cach 1: truyen thống
Array1 = [0, 10, 20, 40, 60]
Array2 = [10,30, 40]

def find_element_1(elements: list, test_elements:list):
    data_to_return =[]
    for element in elements:
        if element in test_elements:
            data_to_return.append(element)
    return data_to_return

my_result_1 = find_element_1(Array1, Array2)
print('-----------Ket qua 1: ', my_result_1)


# cach 2: dung .isin của numpy
def find_elements_useIsIn(elements:list, test_elements: list):
    _elements = np.isin(Array1, Array2)

    return [item for item in _elements if item == True]

my_result_2 = find_elements_useIsIn(Array1, Array2)
print('-----------Ket qua 2: ', my_result_2)

# cach 3: dung in1d
def find_elements_useIn1d(elements:list, test_elements: list):
    _elements = np.in1d(Array1, Array2)
    return _elements

my_result_3 = find_elements_useIn1d(Array1, Array2)
print('-----------Ket qua 3: ', my_result_3)

# cach 4: dung intersect1d
def find_elements_useIntersec1d(elements:list, test_elements: list):
    _elements = np.intersect1d(Array1, Array2)
    return _elements

my_result_4 = find_elements_useIntersec1d(Array1, Array2)
print('-----------Ket qua 4: ', my_result_4)