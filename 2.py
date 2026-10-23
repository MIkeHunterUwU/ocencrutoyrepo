n = int(input())
for i in range(n):
    s = input().split()
    a = int(s[0])
    su = 0
    for i in range(1,4):
        b = int(s[i])
        if b > a:
            su += 1
    
    print(su)
