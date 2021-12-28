import bisect
numbers = [6, 3, 2, 10, 10, 10, -10, -10, 7, 3]
numbers.sort()
left = bisect.bisect_left(numbers,2)
right = bisect.bisect_right(numbers,2)
print(left,right)