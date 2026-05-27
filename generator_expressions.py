#Generate Squares Using Generator
num = (x*x for x in range(0, 11))

for i in num:
    print(i)
   
# Sum of Large Numbers Using Generator
total = sum(x for x in range(1,100001))
print(total)

# Filter Even Numbers Using Generator
even = (x for x in range(1,21) if x%2==0)

for i in even:
    print(i)

# Compare List vs Generator Memory
nums_list = [x for x in range(1, 11)]
nums_gen = (x for x in range(1, 11))

print(nums_list)
print(nums_gen)

