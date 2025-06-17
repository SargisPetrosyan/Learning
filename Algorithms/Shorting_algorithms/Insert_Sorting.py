list_1 = [2, 1, 5, 9, 4, 3, 8, 7, ]
iter = 0

for i in range(1, len(list_1)):  
    j = i
    while j > 0 and list_1[j] < list_1[j - 1]:  
        list_1[j], list_1[j - 1] = list_1[j - 1], list_1[j]
        j -= 1  
        iter +=1
        
print(list_1)
print(f"iter count {iter}")
