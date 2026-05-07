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

