# Uses python2
# Author :: Colathur Vijayan [VJN]
import sys
import array

input = raw_input().split()
a = int(input[0])
b = int(input[1])

if b < 2 :
 print a
 quit()
  
x = 0
y = 1
period = 0

not_done = True
#lt = array.array('L')
lt = []
 
while not_done:
  x, y = y % b, (x + y) % b 
  lt.insert(period,y)
  period = period + 1
  if (x == 0) and (y == 1):
   break  

#print 'period is %d' % period 	

rem = a % period
z = lt[rem - 2]
#print 'scaled down fib index is %d' % rem
#print 'answer is %d' % z
print z



