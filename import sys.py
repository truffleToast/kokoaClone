import sys
x= int(sys.stdin.readline().rstrip())
flag =0
while x>1:
    if x % 3 == 0:
        x = x/3
        flag +=1
    else:
        x= x-1
        flag +=1
    if x % 2 == 0:
        x = x/2
        flag +=1
print(flag) 
