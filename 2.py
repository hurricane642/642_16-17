__author__ = 'student'
A = set('0123456789')
B = set('02468')
C = set('12345')
D = set('56789')
Q=((D.difference(A)).intersection(B.difference(C)))
w=((A.difference(B)).intersection(C.difference(D)))
E=w.union(Q)
print(E)