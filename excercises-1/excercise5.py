# Ex5: Given two matrices (2 nested lists), the task is to write a Python program
# to add elements to each row from initial matrix.
# For example: Input : test_list1 = [[4, 3, 5,], [1, 2, 3], [3, 7, 4]], test_list2 = [[1], [9], [8]]
# Output : [[4, 3, 5, 1], [1, 2, 3, 9], [3, 7, 4, 8]]
data5_list1 = [[4, 3, 5, ], [1, 2, 3], [3, 7, 4]]
data5_list2 = [[1, 3], [9, 3, 5, 7], [8]]


def combine_list(list1:list, list2:list):
    if len(list1) != len(list2):
        print('---error: độ lớn 2 ma trận không bằng nhau')
        return []

    data_to_return = []
    for i in range(len(list1)):
        new_item = list1[i] + list2[i]
        data_to_return.append(new_item)

    return data_to_return


my_result = combine_list(data5_list1, data5_list2)
print('-------my-result:', my_result)