myList = [1, 2, 3, 4, 5]
myList.extend([77, 99, 66, 88])
print('1. ', myList)
myList.sort()
print('2. ', myList)
myList.reverse()
print('3. ', myList)
print('4. ', myList.index(5))
myList.remove(99)
print('5. ', myList)
