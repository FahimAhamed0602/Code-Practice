# Enter your code here. Read input from STDIN. Print output to STDOUT0
from collections import Counter
no_of_shores=int(input())
size_lst=map(int,input().split())
no_of_customers=int(input())
shoes=Counter(size_lst)
income=0
for i in range(no_of_customers):
    size,price=map(int,input().split())
    if shoes[size]:
        income+=price
        shoes[size]-=1
print(income)