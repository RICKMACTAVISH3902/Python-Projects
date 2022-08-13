

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




































# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
