# Ex4: print all Possible Combinations from the three Digits
import itertools

data4 = [1, 2, 3]


# dung de quy va hoan vi
def generate_permutations(numbers, index, permutations):
    if index == len(numbers) - 1:
        permutations.append(numbers.copy())
    else:
        for i in range(index, len(numbers)):
            numbers[index], numbers[i] = numbers[i], numbers[index]
            generate_permutations(numbers, index + 1, permutations)
            numbers[index], numbers[i] = numbers[i], numbers[index]

def print_permutations(numbers):
    permutations = []
    generate_permutations(numbers, 0, permutations)
    return permutations


# cach 2 dung itertools
def generate_permutation_numbers(numbers:list):
    result_to_return = []
    generated_items = itertools.permutations(numbers)
    for item in generated_items:
        result_to_return.append(item)
    return result_to_return



my_result = print_permutations([1,2,3])
print('----result-1 ', my_result)

my_result_2 = generate_permutation_numbers([1,2,3])
print('-----result-2', my_result_2)