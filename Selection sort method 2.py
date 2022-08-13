
A = [15,3,9,2,-5]
n=5
j=0
x=A[0]
for i in range(5):
    if x<A[i]:
        x=A[i]
        j=i
        print(x,j)
