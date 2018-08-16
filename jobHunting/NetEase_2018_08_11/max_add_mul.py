"""
Problem Description
Given three number, a, b and c; two operator, addition and multiplication;
and () to set the priority of these operations, decide a way to form an
arithmetic expression to get the maximum result.
Algorithm
Simply enumerate all the cases, as the number of enumeration is quite limited.
"""
a,b,c = [int(x) for x in input().split()]
x =[a+b*c, a*(b+c), a*b*c, (a+b)*c]
print(max(x))