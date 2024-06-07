# Ex4: Read the entire file story.txt and write a program to print out top 100 words occur most
# frequently and their corresponding appearance. You could ignore all
# punction characters such as comma, dot, semicolon, ...
# Sample output:
# house: 453
# dog: 440
# people: 312
# ...
import re
import numpy as np
from collections import Counter



with open('story.txt') as f:
    line = f.readlines()
    f.close()

list_word = []
for word in line:
    result = re.findall("[a-zA-Z0-9]+", word)
    if len(result) > 0:
        list_word += result

def find_unique_elements(input:list, numb:int):
    counter = Counter(input)
    numb_of_elements = counter.most_common(numb)
    data_to_return =[]
    for word, count in numb_of_elements:
        data_to_return.append((word, count))

    return data_to_return


my_result = find_unique_elements(list_word, 100)

for word, count in my_result:
    print(f'{word}: {count}')