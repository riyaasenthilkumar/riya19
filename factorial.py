num=7
num=int(input("Enter a number:"))
factorial=1
if num<0:
  print("factorial does not exist for negative number")
elif num==0:
  print("the factorial of0 is 1")
else:
  for i in range (1,num+1):
    factorial=factorial*i
print("the factorial of",num,"is",factorial)
