a ,b, c = map(int,input().split())

def sol(a,n):
    if n==1:
        return a%c
    else:
        tmp = sol(a,n//2)
        if a%2:
            return (tmp*tmp*a)%c
        else:
            return (tmp*tmp)%c
    
print(sol(a,b))

def multi (a,n):
  if n == 1:
      return a%c
  else:
      tmp = multi(a,n//2)
      if n %2 ==0:
          return (tmp * tmp) % c
      else:
          return (tmp  * tmp *a) %c
          
print(multi(a,b))