

n = int(input("Enter the number "))
nums = n
tot = 0
while n>0:
    f=1
    num = n % 10
    while num>0:
        f = f*num
        num = num - 1
    tot = tot + f
    n = n // 10
print("The sum of numbers is", tot)
if tot == nums:
    print("The ", nums, "is a strong number ")
else:
    print("Not Strong ")


