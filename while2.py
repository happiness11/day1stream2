def sumnums(n)
   x = 0
   total = 0
   while x<=n:
       total = total + x
       x = x+1
       return total
    print(sumnums(5))