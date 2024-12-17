# #    run python code 
# print("Hello World")

# #   variable are dynamicly typed

# n = 0
# print('n =', n)

# #   multiple assigments
# n, m = 0, 'abc'

# print('n: ',n, 'm: ', m)

# #   Increment
# a = 1
# print(a)
# a = a+1 
# print(a)
# a += 1
# print(a)

# #   None is null (absence of value)
# n = 4
# print(n)
# n = None
# print(n)

# #   if statement 
# #   if statement don't need parentheses
# #   or curly braces
# n = 3
# if n > 2:
#     n -= 2
# elif n == 2:
#     n *= 2
# else:
#     n += 2

# print(n)

# #   parentheses needed for multi-line conditions.
# #   and = &&
# #   or = ||

# n = 3
# m= 3
# if ((n > 2 and n != m) or n == m):
#     n += 1
# print(n)    

# #    while loop

# n = 0
# while n < 5:
#     print(n)
#     n += 1


# for i in range(5):
#     print(i)

# #   looping from i = 2 to i = 5
# for i in range(2, 6):
#     print(i)

# #   looping from i = 5 to i = 2
# for i in range(5, 1, -1):
#     print(i)

# #   Math

# #   Division is decimal by defualt
# print(5/2)

# #   Double slash rounds down
# print(5//2)

# #   BeCarefull: most languages round towards 0 by 
# #   default so negative numbers will round down
# print(-3 // 2)

# #   A workaround for rounding towards zero is to 
# #   use decimal division and then convert to int.
# print(int(-3/2))

# #   Modding is similar to most languages
# print(10%3)

# #   Except for negative values
# print(-10 % 3)

# #   Math helper

# import math

# print(math.floor(3/2))
# print(math.ceil(3/2))
# print(math.sqrt(25))
# print(math.pow(2,3))

# #   Max /Min
# float("inf")
# float("-inf")

# import math
# print(math.pow(2, 200))

# print(math.pow(2, 200) < float("inf"))

# #   Array
# arr = [1, 2, 3]
# print(arr)

# #    Can be use as a stack
# arr.append(4)
# arr.append(4)
# print(arr)
# arr.pop()
# print(arr)

# arr.insert(2, 333) #    This is Big of N
# print(arr)

# arr[2] = 0 #    constain time oparetion
# print(arr)

# #    Initialze arr if size n with defualt value of 1
# n = 5
# arr = [1] * n
# print(arr)
# print(len(arr))

# #   Careful: -1 is not out of bounds,
# #   it's the last value
# arr = [1,2,3]
# print(arr[-1])

# #   Sublist (aka slicing)
# arr = [1,2,3,4]
# print(arr[1:3]) #    index 1 to index 3 (but not include index 3)

# #    unpacking
# a, b, c = [1, 2, 3]
# print(a)
# print(b)
# print(c)

# #    Be careful though
# a, b = [1, 2, 3]
# print(a)
# print(b)


# #   Loop through arrays
# nums = [1,2,3]

# #   Using index
# for i in range(len(nums)):
#     print('inde: ', i, 'values: ', nums[i])


# #   looping list without index
# for n in nums:
#     print(n)

# #   with index and value
# for i, n in enumerate(nums):
#     print(i,n)    


# #   Zip multiple array
# nums1 = [1,2,3]
# nums2 = [4,5,6]
# nums3 = [7,8,9]

# for n1, n2, n3 in zip(nums1, nums2, nums3):
#     print(n1, n2, n3)


# #   sorting

# arr = [5, 4, 7, 3, 8]
# print(sorted(arr))
# print(arr)
# arr.sort()
# print(arr)

# # reverse sort
# arr.sort(reverse=True)
# print(arr)

arr = ['bob', 'alice', 'jane', 'doe']
# arr.sort()
# print(arr)

# sorting by length of string
arr.sort(key = lambda x: len(x))
print(arr)