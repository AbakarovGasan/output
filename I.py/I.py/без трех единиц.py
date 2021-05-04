
def fib(n):
  a,b=0,1
  for i in range(n):
    x=b
    b=a
    a=a+x
  return a
n=int(input())
print(fib(n+1)+fib(n)+fib(n-1))

    
               
