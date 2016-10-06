__author__ = 'student'
import numpy as np
def get_percentile(values, bucket_number):
    percentiles=[]
    for i in range(0, bucket_number):
        if i==0:
            perc_i=0.0
        else:
            p_i=i*100/bucket_number
            perc_i=np.percentile(value, p_i)
            percentiles.append(perc_i)
        return percentiles