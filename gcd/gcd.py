# Uses python2
# Author :: Colathur Vijayan [VJN]
import sys

input = raw_input().split()
a = int(input[0])
b = int(input[1])

current_gcd = 1

if a == 0 :
  print b
  quit()
elif b == 0 :
  print a
  quit()

if a == b:
  print a
  quit()
  
not_done = True

while not_done :
  c = min(a, b)
  d = max(a, b) % c
  a = min(c, d)
  b = max(c, d)
  if a == 0:
    not_done = False

print b
