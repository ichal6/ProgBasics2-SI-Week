import math
import pandas as pd

def fibo(size):
    i = 0
    j = 1
    k = 0
    lst = []
    fib = 0
    while i < size:
        lst.append(fib)
        fib = j + k
        j=k
        k=fib
        i=i+1
    
    df = pd.DataFrame(lst)
    df.index = df.index + 1
    df.columns = ["Value:"]
    print(df)

user_number=102
user_number = int(input('Please input how many number of Fibonacii screen: '))
n=0

fibo(user_number)