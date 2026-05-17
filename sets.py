# Remove Duplicates from List
nums = [4, 2, 4, 1, 2, 3, 1, 5]
n = list(set(nums))#we cannot sort in set so we use list
print(n)

# Find Intersection of Two Lists
a = [7, 2, 5, 2, 9, 1]
b = [5, 2, 8, 1, 1]

print(set(a)&set(b))#we can't use& directly to list

# Find Union of Two Lists
a = [4, 1, 7]
b = [2, 7, 3, 1]
print(set(a)|set(b))#all elements in both set but once

# Check if Two Lists Have Common Elements
a = [10, 20, 30]
b = [5, 15, 25, 30]
if set(a)& set(b):
    print(True)
else:
    print(False)

# Find Difference Between Two Sets
a = [1, 2, 3, 4, 5]
b = [2, 4]
print(set(a)-set(b))

# Check Subset / Superset
required = {"read", "write"}
user = {"read", "write", "delete", "share"}

print(required.issubset(user))

# Count Unique Words in Sentence
sentence = "Python is Easy and python is Powerful"
word = sentence.lower().split()#set treat upper lower case are difffrent
unique = set(word)
print(len(unique))