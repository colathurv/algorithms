# Uses python2
# Author :: Colathur Vijayan [VJN]
import sys
import array

WArray = []
isFirstRow  = True
v =[]

while True:
    line = sys.stdin.readline().rstrip('\n')
    if line == '':
        break
    elif isFirstRow:
        line = line.split()    
        W = int(line[0])
        n = int(line[1])
        isFirstRow = False 
    else:
        line = line.split()
        for i in range(n):
            WArray.append(int(line[i]))


def knapSack(W, w, v, n):
    K = [[0 for x in range(W+1)] for x in range(n+1)]
    
    #print '------In Knapsack ----'
    #print K
    #print w
 
    
    # Initialize
    for i in range(n+1):
        K[i][1] = 0
    
    for j in range(W+1):
        K[1][j] = 0
        
    #print '--- Value Matrix at Initialization----'
    #print K
               
    # Build the Value Matrix K bottom up
    for i in range(1, n+1):
        for j in range(1, W+1):
            #print i
            #print j
            K[i][j] = K[i-1][j]
            if w[i - 1] <= j:
                #print '---------'
                #print i
                #print w[i - 1]
                val = K[i - 1][j - w[i - 1]] + v[i - 1]
                if K[i][j] < val:
                   K[i][j] = val
    #print '--- Value Matrix after Calculation ----'
    #print K
    return K[n][W]

v = WArray

#print '---Variable dump before calling knapsack ---'
#print W
#print WArray
#print v
#print n

x = knapSack(W, WArray,v,n)
#print '-- Max Weight --'
print x


