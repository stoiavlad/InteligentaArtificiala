def sum_lists(list1, list2):
    rezultat = []

    for a, b in zip(list1, list2):
        rezultat.append(a + b)

    return rezultat

list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30, 40, 50]

result = sum_lists(list1, list2)
print(result)