# Ex3: find the strongest neighbour. Given an array of N positive integers.
# The task is to find the maximum for every adjacent pair in the array.
data3 = [4, 5, 6, 7, 3, 9, 11, 2, 10]


def find_strongest_neighbour(numbers:list):
    data_to_return = []
    for i in range(len(numbers)):

        if i < len(numbers) -1: # nếu là phần tử cuối thì không so sánh nữa
            strongest_numb = max(numbers[i], numbers[i +1])
            data_to_return.append(strongest_numb)

    return data_to_return


my_result = find_strongest_neighbour(data3)
print('-----Ket qua:', my_result)