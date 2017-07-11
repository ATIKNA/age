import sys


n = int(input().strip())
a = list(map(int,raw_input().strip().split(' ')))

print(max(a.count(x)+a.count(x+1) for x in set(a)))
