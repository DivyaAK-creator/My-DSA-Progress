n=1234
total = 0
while n>0:
    digit = n % 10#takes last digit
    total = total + digit 
    n = n // 10  #removes last digit

print(total)

n = 123
original = n
total = 0
while n>0:
    digit = n%10
    total = total + digit**3
    n = n//10

if total == original:
    print("Armstrong")
else:
    print("Not Armstrong")
# palindrom or not
n = 121
original = n
rev = 0
while n>0:
    digit = n%10
    rev = rev*10+digit
    n = n//10
if rev == original:
    print("Palindrom")
else:
    print("Not Palindrom")
# prime number
n = 25
is_prime = True

for i in range(2,int(n**0.5)+1):
    if n%i==0:
      is_prime = False
      break
if n<0:
    print("Not prime")
elif is_prime:
    print("prime")
else:
    print("Not prime") 

arr = [2, 8, 1, 10, 3, 7]
count = 0

for num in arr:
    if num>5:
        count=count+1
print (count)



n=1234
total = 0
while n>0:
    digit = n % 10#takes last digit
    total = total + digit 
    n = n // 10  #removes last digit

print(total)

n = 123
original = n
total = 0
while n>0:
    digit = n%10
    total = total + digit**3
    n = n//10

if total == original:
    print("Armstrong")
else:
    print("Not Armstrong")
# palindrom or not
n = 121
original = n
rev = 0
while n>0:
    digit = n%10
    rev = rev*10+digit
    n = n//10
if rev == original:
    print("Palindrom")
else:
    print("Not Palindrom")
# prime number
n = 25
is_prime = True

for i in range(2,int(n**0.5)+1):
    if n%i==0:
      is_prime = False
      break
if n<0:
    print("Not prime")
elif is_prime:
    print("prime")
else:
    print("Not prime") 

arr = [2, 8, 1, 10, 3, 7]
count = 0

for num in arr:
    if num>5:
        count=count+1
print (count)

# find duplicates in array

arr=[3,7,2,9,5]
max_val = arr[0]

for num in arr:
    if num > max_val:
        max_val = num
        print(max_val)