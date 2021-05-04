def fib(n):
  a,b=0,1
  for i in range(n):
    x=b
    b=a
    a=a+x
  return a
print(fib(int(input())+2))

