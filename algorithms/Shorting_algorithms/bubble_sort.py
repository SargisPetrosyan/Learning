list_1 = [2, 1, 5, 9, 6, 4, 3, 8, 7]
iter = 0
for i in range(len(list_1) - 1):
    for j in range(len(list_1) - i - 1):
        sorting = False
        if list_1[j] > list_1[j + 1]:
            list_1[j], list_1[j + 1] = list_1[j + 1], list_1[j]
            sorting = True
        if sorting is False:
            continue
        iter += 1

print(list_1)
print(f"iter count {iter}")
