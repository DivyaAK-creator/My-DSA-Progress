# Square All Numbers in List
nums = [3, -2, 5, -7, -1, 4]
num = [x*x for x in nums if x<0]#square of only negative numbers
print(num)

# Filter Even Numbers
nums = [4, 11, 18, 7, 24, 9, 14]
num = [x for x in nums if x%2==0 and x>10]
print(num)

# Create List of Tuples (number, square)
nums = [1, 2, 3, 4, 5]
num = [(x,x*x*x) for x in nums if x%2!=0]
print(num)

# Flatten Nested List
nested = [[2, 8], [1, 6, 3], [9, 4]]
list=[item for sublist in nested for item in sublist if item>5 ]
print(list)

# Remove Vowels from String
text = "Python is powerful"
vowels = "".join([ch for ch in text if ch not in "aeiou "])#space is for remove extra space
print(vowels)

# Conditional List Creation
nums = [1, 2, 3, 4, 5]
num=["Even" if x%2==0 else x*x for x in nums]
print(num)
