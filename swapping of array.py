

A = [5,3,9,2,-5]
n = 5
j = 0
for i in range(n):
    a = A[i]
    m=j
    for j in range(i,n):
        if A[i]>a:
            a=A[i]
            m=j
t = A[i]
a = A[i]
t = A[m]
print(m,t)
