# Ex1: Write a NumPy program to reverse an array (first element becomes last).
# Input: [12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37]
import numpy as np

Input = [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37]

def revert_list(input:list):
    data_to_return = input.copy()
    data_to_return.reverse()
    return data_to_return

print('------ket quả = ', revert_list(Input))


#--cach 2 dùng numPy
def numpy_revert(input:list):
   return np.flip(input, axis=None)

print('-----Ket quả 2: ', numpy_revert(Input))


#--- cách 3
def revert_list_3(input:list):
    return input[::-1]
print('-------ket quả 3: ', revert_list_3(Input))