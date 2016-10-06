__author__ = 'student'
import random

def f(x):
    if -2<=x and x<=2:
        return -x**2 + 4
    else:
        return 0
random.seed()
n=10000
s=0
for i in range(n):
    x=random.uniform(-3, 3)
    s+=6/n*f(x)
print(s)
