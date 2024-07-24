import numpy
import pandas as pd
import math

def multiply_list(intstr):
    l1=intstr.split()
    result=1
    if len(l1)>0:
        for i in l1:
            result=result*int(i)
        return result
    else:
        return 0
    
def count_common_chars(str2):
    set1={*set()}
    l1=str2.split()
    if len(l1)==2:
        for i in l1[0]:
            if i in l1[1]:
                set1.update(i)
    return len(set1)

def sum_divisible_by_k(n,k):
    if k==0 or n==0 or n<k:
        return -1
    else:
        sum=0
        l1=[]
        for i in range(1,n+1):
            l1.append(i)
            if i%k==0:
                sum=sum+i
        return sum
    
def highest_common_factor(n1,n2):
    fact1=[]
    fact2=[]
    cfact=[]
    for i in range(1,n1+1):
        if n1%i==0:
            fact1.append(i)
    for i in range(1,n2+1):
        if n2%i==0:
            fact2.append(i)
    for i in fact1:
        if i in fact2:
            cfact.append(i)
    return max(cfact)

def get_minimum(list1):
    return min(list1)

def rename_col(df1,cold,cnew):
    df1.rename(columns={cold:cnew},inplace=True)
    return df1

def standard_deviation(l1):
    n=len(l1)
    sum=0
    sum1=0
    for i in l1:
        sum=sum+i
    avg=sum/n
    for i in l1:
        sum1=sum1+(i-avg)**2
    stddev=math.sqrt(sum1/n)
    return stddev

def correlation_sum(l1):
     if len(l1)!=9:
         return 0
     else:
         arr = numpy.array(l1).reshape((3,3))
         df1=pd.DataFrame(arr)
         corr1=df1.corr().round(2)
         correlationAB = df1[0].corr(df1[1])
         correlationBC = df1[1].corr(df1[2])
         correlationAC = df1[0].corr(df1[2])
         mat=numpy.matrix(correlationAB,correlationBC,correlationAC)
         sum=correlationAB+correlationBC+correlationAC         
         return round(sum,2)
