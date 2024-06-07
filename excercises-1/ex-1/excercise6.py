# Ex6:  Write a program which will find all such numbers which are divisible by 7
# but are not a multiple of 5, between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.

def find_numbers_divisible_by(start: int, end: int, so_bi_chia: int, uoc_so: int):
    if so_bi_chia == 0:
        print('---error: số bị chia không được bằng 0')
        return None

    if start == end and start % so_bi_chia == 0 and start % uoc_so != 0:
        return str(start)
    elif start == end and start % so_bi_chia == 0 and start % uoc_so == 0:
        return None
    elif start == end and start % so_bi_chia != 0:
        return None

    result_to_return = []
    for i in range(start - 1, end + 1):
        if i % so_bi_chia == 0 and i % uoc_so != 0:
            result_to_return.append(i)

    return result_to_return


my_list = find_numbers_divisible_by(2000, 3200, 7, 5)

result_str = ''
for x in my_list:
    result_str += str(x) + ','

print('-----Ket qua:', result_str)
