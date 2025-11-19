from time import time

start_time = time()
x = [x**2 for x in range(10000000)]
comprehension_end = time()-start_time

list = []
for x in range(10000000):
    list.append(x**2)
for_loop_end = time()- start_time

print(f'comprehension: {comprehension_end}, for_loop:{for_loop_end} ')