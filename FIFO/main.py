from FIFO.Queue import *
from FIFO.Element import *

if __name__ == "__main__":
    myQueue = Queue()

    myQueue.push(Element(1))
    myQueue.push(Element(2))
    myQueue.push(Element(3))
    myQueue.push(Element(4))
    myQueue.push(Element(5))

    print(str(myQueue.pop().getValue()))
    print(str(myQueue.pop().getValue()))
    print(str(myQueue.pop().getValue()))
    print(str(myQueue.pop().getValue()))
    print(str(myQueue.pop().getValue()))
    print(str(myQueue.pop()))