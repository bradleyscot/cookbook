
from pythonds.basic.stack import Stack

def revstring(mystr):
    myStack = Stack()
    for i in mystr:
      myStack.push(i)
      revstr = ''
    while not myStack.isEmpty():
      revstr = revstr + myStack.pop()
    return revstr

print('apple:', revstring('apple'))
print('x:', revstring('x'))
print('1234567890:', revstring('1234567890'))