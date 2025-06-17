list_1 = [2, 1, 5, 9, 6, 4, 3, 8, 7]
iter = 0

for i in range(len(list_1) - 1):
    min_idx = i
    j = i + 1
    while j < len(list_1):
        if list_1[j] < list_1[min_idx]:  
            min_idx = j
        j += 1
        iter += 1 


    list_1[i], list_1[min_idx] = list_1[min_idx], list_1[i]
        
print(list_1)
print(f"iter count {iter}")
        