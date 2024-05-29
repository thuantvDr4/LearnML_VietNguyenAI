# Ex1: Write a program to count positive and negative numbers in a list

data1 = [-10, -21, -4, -45, -66, 93, 11, -4, -6, 12, 11, 4]

positive_items =[]
negative_items =[]

for item in data1:
    if item > 0:
        positive_items.append(item)
    else:
        negative_items.append(item)

print('---positive numbers:', len(positive_items))
print('---negative numbers:',len(negative_items))