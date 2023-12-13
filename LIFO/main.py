from LIFO.Stack import *
from LIFO.Element import *

if __name__ == "__main__":
    myStack = Stack()

    myStack.push(Element(1))
    myStack.push(Element(2))
    myStack.push(Element(3))
    myStack.push(Element(4))
    myStack.push(Element(5))

    print(str(myStack.pop().getValue()))
    print(str(myStack.pop().getValue()))
    print(str(myStack.pop().getValue()))
    print(str(myStack.pop().getValue()))
    print(str(myStack.pop().getValue()))
    print(str(myStack.pop()))