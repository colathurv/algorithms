# Uses python2
# Author :: Colathur Vijayan [VJN]
import sys
import array

input = int(raw_input())
r1 = input % 10
q1 = input/10

if r1 == 0:
 print q1
 quit()
else:
 r2 = r1 % 5
 q2 = r1/5
 if r2 == 0:
  print q1 + q2
  quit()
 else:
  print q1 + q2 + r2