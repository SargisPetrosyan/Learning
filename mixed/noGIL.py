"""
Simple demonstration of multithreading with a CPU-bound task in Python.
"""
import time
import threading

def compute()->None:
    """
    Performs a summation of integers from 0 up to 10 million (exclusive).
    """
    total = 0
    for i in range(10**7):
        total += i


def multithreading()-> None:
    """
    Runs the compute function in 4 separate threads to 
    demonstrate multithreading with CPU-bound tasks.
    """
    threads = []
    for _ in range(4):
        t = threading.Thread(target=compute)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

# output with GIL 1.502
# output without GIL 0.590
start = time.time()
compute()
end_task = time.time()-start
print(f"without multithreading seconds: {end_task:.6f}")

start_task_2 = time.time()
multithreading()
end_task_2 = time.time()-start_task_2
print(f"with multithreading seconds: {end_task_2:.6f}")