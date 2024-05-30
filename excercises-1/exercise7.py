# Ex7: Write a program, which will find all such numbers between 1000 and 3000 (both included)
# such that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.

def find_numbers_even(start:int, end:int):

    if start == end and start % 2 == 0:
        return start
    elif start == end and start % 2 != 0:
        return None

    data_to_return = []
    for i in range(start-1, end+1):
        if i % 2 == 0:
            data_to_return.append(i)

    return data_to_return


my_list = find_numbers_even(1000, 3000)

result_str = ''
for x in my_list:
    result_str += f'{x},'


print('-----Ket qua:', result_str)