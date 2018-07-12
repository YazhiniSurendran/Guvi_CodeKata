'''num1 = int(input())
num2 = int(input())
num3 = int(input())


if num1 > num2:
  if num1 > num3:
    print(num1)
  elif num2 > num3:
  	print(num2)
else:
  print(num3) '''

a = input()
a = a.split()
num1 = a[0]
num2 = a[1]
num3 = a[2]

if num1 > num2:
  if num1 > num3:
    print(num1)
  elif num2 > num3:
  	print(num2)
else:
  print(num3)
