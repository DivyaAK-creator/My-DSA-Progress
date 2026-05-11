# Swap Two Variables Using Tuple
a = 10
b = 20
c = 30

a,b,c = b,c,a
print(f"a={a}\nb={b}\nb={c}")

# Count Occurrences of Element
t = (1, 2, 3, 2, 4, 2, 5, 2)
count = t.count(2)
print(count)
print(count>len(t)/2)
# if t.count(2)>len(t)/2:
#     print("True")
# else:
#     print("False")

# Convert List ↔ Tuple
nums = [1, 2, 3, 4, 5]
num = tuple(nums)
print(num)
n = list(num)
print(n)
n.append(6)
print(n)
number = tuple(n)
print(number)

# Find Max and Min in Tuple
t = (12, 45, 2, 89, 34, 89, 5)
Max =max(t)
Min =min(t)
print("Max=",Max)
print("Min=",Min)
print("Difference=",Max-Min)
s = set(t) # remove duplicates
l = list(s)#convert into list to do sorting
l.sort()
print(l[-2])

# Tuple Unpacking with Multiple Values
data = ("Alice", 21, "Python", "DSA", "AI", 95)
name,age,*subjects,marks = data
print(name)
print(age)
print(subjects)
print(marks)