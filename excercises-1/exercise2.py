# Ex2: Given a list, extract all elements whose frequency is greater than k.

data2 = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
k = 3


# function to find elements that pass condition
def findElements(elements: list):
    elements_to_return = []
    for item in elements:
        if elements.count(item) > k:
            elements_to_return.append(item)

    return elements_to_return


# cal function
my_elements = findElements(data2)
print(f'----the elements whose frequency is greater than {k}: ', my_elements)
