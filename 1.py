__author__ = 'student'
import numpy
values = [3, 4, 1, 2, 5, 6, 7, 8, 9, 10]
bucket_number=int(input())
for i in range(bucket_number):
    if i*100/bucket_number==0:
        print(0.0, end=" ")
    else:
        print(numpy.percentile(values, i*100/bucket_number), end=" ")