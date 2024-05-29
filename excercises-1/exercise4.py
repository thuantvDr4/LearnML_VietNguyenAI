# Ex4: print all Possible Combinations from the three Digits
data4 = [1, 2, 3]


def find_permutation_items(data: list):
    if len(data) == 0:
        return []
    if len(data) == 1:
        return data
    #
    items_to_return = []
    for i in range(len(data)):
        current_item = data[i]
        remaining_items = data[:i] + data[i + 1:]
        print('---current', current_item)
        print('---remaining', remaining_items)

        for item in find_permutation_items(remaining_items):
            print(f'----item={i}', item)

            my_items = [current_item] + [item]
            print(f'----my_items={i}', my_items)
            items_to_return.append(my_items)
            print('----end-loop', items_to_return)
    return items_to_return


my_result = find_permutation_items([1, 2, 3])
print('----result', my_result)
