#reverse list
n = [1,2,3,4,5]
n.sort(reverse = True)
print(n) 
#or
print(n[::-1])

#Find Second Largest Number
num = [10,50,20,40]
num.sort(reverse=True) #50,40,20,10
print(num[1]) #40

# Remove Duplicates
nums = [1, 2, 2, 3, 1, 4]
nums = list(set(nums)) #it give set in list set holds only unique value
print(nums)

#Merge Two Sorted Lists
a = [1, 3, 5]
b = [2, 4, 6]
c = (a+b)
c.sort()
print(c)

# Move Zeros to End
nums = [1,0,2,0,1]
non_zero =[]
zero =[]

for i in nums:
    if i==0:
        zero.append(i)
    else:
        non_zero.append(i)

print(non_zero+zero)

# Check Palindrome List
nums = [1, 4, 3, 2, 1]

if nums == nums[::-1]:
    print("Palindrome")
else:
     print("Not Palindrome")

#Rotate List Left (Move the first element to the end)
n = [1,2,3,4,5,6,7]
original = n.copy()
while True:
    n = n[1:]+[n[0]]
    print(n)
    if n == original:
     break

# Find Pairs with Given Sum
num = [1,2,3,4,5]
target = 6

for i in range(len(num)):
    for j in range(i+1,len(num)):
        if num[i]+num[j]==target:
            print(num[i],num[j])

# Flatten Nested List
nums = [[1,2],[3,4],[5]]
flat = []
for sublist in nums:
    for item in sublist:
        flat.append(item)
print(flat)