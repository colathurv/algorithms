# Uses python2
# Author :: Colathur Vijayan [VJN]
import sys


def getKey(item):
    return item[1]

isFirstRow  = True
n = 0
lt = []
index = 0
minCovering = []

while True:
    line = sys.stdin.readline().rstrip('\n')
    if line == '':
        break
    elif isFirstRow:    
        n = int(line)
        isFirstRow = False 
    else:
        line = line.split()
        lt.insert(index,[int(line[0]), int(line[1])])
        index = index + 1


lt = sorted(lt, key=getKey)
 
#print n
#print lt

for i in range(n):
    if i == 0:
        #print 'adding for i = 0'
        minCovering.append(lt[0][1])
        #print minCovering
        #print '----'
    else:
        #print 'in else ...'
        if not lt[i][0] <= minCovering[-1] <= lt[i][1]:
            #print 'adding ..'
            minCovering.append(lt[i][1])
        #print 'exiting else ...'
            
#print minCovering
print len(minCovering)
print ' '.join(map(str, minCovering))