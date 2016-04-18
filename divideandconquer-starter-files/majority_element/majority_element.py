# Uses python2
# Author :: Colathur Vijayan [VJN]
import sys
import array


# Crux of the problem is that a majority element, if one such exists
# its occurence will be dense enough that pairwise comparison scores
# will always prevail [i.e., be positive] when going from left to right.

isFirstRow  = True
found = False
not_done = True
A = []
n = 0 
maj_index = 0
count = 1

while not_done:
    line = sys.stdin.readline().rstrip('\n')
    if isFirstRow:
        line = line.split()    
        n = int(line[0])
        isFirstRow = False 
    else:
        line = line.split()
	for i in range(n):
            A.insert(i,int(line[i]))
        not_done = False
   

for i in range(2, n):
    if A[i] == A[maj_index]:
        count = count + 1
    else:
        count = count - 1
        
    if count == 0:
        maj_index = i
        count = 1
 
count = 0
k = A[maj_index]

for i in range(n):
    if A[i] == k :
        count = count + 1
     
if count > n/2:
    print 1
else:
    print 0
            
            
            