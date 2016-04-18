# Uses python2
# Author :: Colathur Vijayan [VJN]
import sys

n = int(raw_input())
k = 0
not_done = True
A = []

if n == 2:
    print 1
    print 2
    quit()
    
while not_done :
    k = k + 1
    u = (k * (k + 1))/2
    
    #print 'u = %d' % u
    if u == n:
        #print 'k = %d' % k
        for i in range(k):
            A.append(i + 1)
        break
    
    if u > n:
        t = n - ((k - 1) * k)/2
        for i in range(k-1):
	    A.append(i + 1)
	    
        if not t in A:
            A.append(t)
        else:
            A[k-2] = k - 1 + t
        break
 
print len(A) 
print ' '.join(map(str, A))