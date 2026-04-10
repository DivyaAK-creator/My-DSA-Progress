
n = int(input("n: "))
if n % 2 != 0:
    print("Weird")
elif 2<=n<=6:#Q.even num btw 2 to 6 but we dont write even condition because rather than even we right odd it shows Weird as per first condition
    print("Not Weird")
elif 6<=n<=20:
    print("Weird")
else:
    print("Not Weird")

m = int(input("m: "))
if m<0 or m>100:
    print("Invalid")
elif m == 100:
    print("perfect Score")
elif m >= 90:
    print("A+")
elif m >= 75:
    print("B+")
elif m >= 50:
    print("C+")
elif m >= 35:
    print("D+")
else:
    print("Fail")


a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))

if a<=0 or b<=0 or c<=0:
    print("Invalid Triangle")
if a + b<= c or b+c<=a or c+a<=b:
         print("Invalid Triangle")
if a == b == c:
              print("Equilateral")
elif a == b or b == c or c == a:
    print("Isosceles")
else:
     print("NOT triangle")
  

n = int(input("n: "))
if n % 2 != 0:
    print("Weird")
elif 2<=n<=6:#Q.even num btw 2 to 6 but we dont write even condition because rather than even we right odd it shows Weird as per first condition
    print("Not Weird")
elif 6<=n<=20:
    print("Weird")
else:
    print("Not Weird")

m = int(input("m: "))
if m<0 or m>100:
    print("Invalid")
elif m == 100:
    print("perfect Score")
elif m >= 90:
    print("A+")
elif m >= 75:
    print("B+")
elif m >= 50:
    print("C+")
elif m >= 35:
    print("D+")
else:
    print("Fail")


a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))

if a<=0 or b<=0 or c<=0:
    print("Invalid Triangle")
if a + b<= c or b+c<=a or c+a<=b:
         print("Invalid Triangle")
if a == b == c:
              print("Equilateral")
elif a == b or b == c or c == a:
    print("Isosceles")
else:

    print("Scalene")