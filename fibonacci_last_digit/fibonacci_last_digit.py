# Uses python2
# Author :: Colathur Vijayan [VJN]

n = int(raw_input())
if n < 2 :
  print n
  quit()

x = 0
y = 1
k = 1	

while k < n:
  x, y = y % 10, (x + y) % 10
  k = k + 1

print y
