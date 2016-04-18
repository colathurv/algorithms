# Uses python2
# Author :: Colathur Vijayan [VJN]
import sys
import array

WArray = []
isFirstRow  = True
str1 = ''
str2 = ''
insertion = 0
deletion = 0
match = 0
mismatch = 0

while True:
    line = sys.stdin.readline().rstrip('\n')
    if line == '':
        break
    elif isFirstRow:
        str1 = line
        isFirstRow = False 
    else:
        str2 = line

n = len(str1) + 1
m = len(str2) + 1

#print n
#print m

D = [[0 for x in range(m)] for x in range(n)]

for i in range(n):
    D[i][0] = i

for j in range(m):
    D[0][j] = j
    
#print D

for j in range(1, m):
    for i in range(1, n):
            #print '----------'
            #print i
            #print j
            insertion = D[i][j - 1] + 1
            deletion  = D[i - 1][j] + 1
            match = D[i - 1][j - 1]
            mismatch = D[i - 1][j - 1] + 1
            if str1[i-1] == str2[j-1]:
                D[i][j] = min(insertion, deletion, match)
            else:
                D[i][j] = min(insertion, deletion, mismatch)

            #print '--------'
            #print str1[i-1]
            #print str2[j-1]
            #print D
print D[n-1][m-1]