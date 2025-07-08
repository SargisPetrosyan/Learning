# create iterator class
class MyIterator:
    """same as call iter(num)"""

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= self.end:
            raise StopIteration
        else:
            current = self.start
            self.start += 1
            return current


nums = MyIterator(1, 10)


# doing same as for loop
while True:
    """for nums in num:
            print(num)"""
    nums = MyIterator(1, 10)

    try:
        item = next(nums)
        print(item)
    except StopIteration:
        break

print(dir(MyIterator))


def generator(start):
    """Generator"""
    current = start
    while True:
        yield current
        current += 1


nums = generator(1)

for num in nums:
    print(num)
