t = int(input())
for _ in range(t):
     a, b, c = map(int, input().split())
     while 1<=a<=9 and 1<=b<=9 and -8<=c<=18:
          if a+b==c:
              print("+")
          elif a-b==c:
               print("-")
               
