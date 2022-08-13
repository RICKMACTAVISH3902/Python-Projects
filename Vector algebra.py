#Vector
#Vector additon of array
A=[1,3,4]
B=[2,0,3]
C=[]
for i in range(3):
    C.append(A[i]+B[i])
print(C)

#Dot Product
D=0
for i in range(3):
    D+=(A[i]*B[i])
print(D)

#Modulus of vector
modA=0
modB=0
for i in range(3):
    modA+=A[i]**2
    modB+=B[i]**2
modA=modA**0.5
modB=modB**0.5
print(modA,modB)

#Angle between two vectors
import math as mt
angle=mt.acos(D/(modA*modB))
print(angle)


