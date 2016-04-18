# Uses python2
# Author :: Colathur Vijayan [VJN]
import sys
import array
from decimal import *

VArray = []
WArray = []
QArray = []
isFirstRow  = True
index = 0

while True:
    line = sys.stdin.readline().rstrip('\n')
    if line == '':
        break
    elif isFirstRow:
        line = line.split()    
        n = int(line[0])
        W = int(line[1])
        isFirstRow = False 
    else:
        line = line.split()
        VArray.insert(index,int(line[0]))
        WArray.insert(index,int(line[1]))
        QArray.insert(index,Decimal(int(line[0]))/Decimal(int(line[1]))) 
        #print QArray
        index = index + 1


V = Decimal(0.0)
A = []
a = 0

for i in range(n):
    A.append(0)
    
for i in range(n):
    #print 'Index %d' % i
    if W == 0:
        break
    max_value = max(QArray)
    k = QArray.index(max_value)
    #print 'k is %d' % k
    a = min(WArray[k], W)
    #print 'a is %d ' % a
    #print VArray[k]
    #print WArray[k]
    getcontext().prec = 10
    V = V + Decimal((a * VArray[k]))/Decimal(WArray[k])
    WArray[k] = WArray[k] - a
    QArray[k] = 0
    A[k] = A[k] + a
    W = W - a

print '%.4f' % V 