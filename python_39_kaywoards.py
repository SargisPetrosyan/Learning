"""
False+      await+      else+       import+     pass+
None+       break+      except+     in+         raise+
True+       class+      finally+    is+         return+
and+        continue+   for+        lambda+     try+
as+         def+        from+       nonlocal+   while+
assert+     del+        global+     not +       with+
async+      elif+       if+         or+         yield+

"""

# as
import time as t


# finally
try:
    file = open("test.txt", "w")
    file.write("Hello, World!")
    print("File written successfully.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    file.close()
    print("File closed.")

# continue
for _ in range(10):
    if _ % 2 == 0:
        continue
    else:
        print(_)

# lamda
x = lambda x, y: x + y
print(x(3, 4))


# nonlocal
def counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment


c = counter()
print(c())  # Output: 1
print(c())  # Output: 2
print(c())  # Output: 3


# assert
def checkdb():
    x = 5
    y = 4
    assert 5 % 4 == 0


# checkdb()

# del
z = [2, 4, 5, 6, 7]
print(z)
del z

# global
h = 10


def cal_h():
    global h
    print(h + 1)


cal_h()
