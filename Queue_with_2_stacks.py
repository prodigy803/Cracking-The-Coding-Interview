"""
We have to essentially implement a queue ds with the help of two stacks

Solution:
We can build two stacks.
Here we add the elements as we would in a normal stack
Once all the elements are added, we will lifo those elements to the other stack (where in the first elements will be out first)
the second stack will be our queue

Now say once we have 'lifo'ed' the elements from one stack to another, if we get additional push's, we will use the first stack to store that
and once the second stack is empty, we will lifo out the elements from the first stack to the second stack
"""

class Node:

    def __init__(self,value = 0):
        self.value = value
        self.next = None
        self.previous = None

class stack:
    def __init__(self):
        self.tail = None
        self.length = 0

    def push(self,value = 0):
        temp_node = Node(value)

        if self.tail == None:
            self.tail = temp_node
        
        else:
            self.tail.next = temp_node
            temp_node.previous = self.tail
            self.tail = temp_node

        self.length +=1

    def pop(self):

        value_to_be_returned = self.tail.value

        if self.tail.previous != None:

            self.tail = self.tail.previous
            self.tail.next = None
        
        elif self.tail.previous != None:
            self.tail = None
        self.length -=1

        return value_to_be_returned

class Queue_from_Stacks:

    def __init__(self):
        self.stack1 = stack()
        self.stack2 = stack()

    def queue(self,value):
        self.stack1.push(value)

    def dequeue(self):
        if self.stack2.length > 0:
            return self.stack2.pop()
        elif self.stack1.length > 0:
            
            while self.stack1.length > 0:
                popped = self.stack1.pop()
                self.stack2.push(popped)
            
            return self.stack2.pop()

        else:
            if self.stack2.length == 0:
                return "Everything is empty"
                
        
queue = Queue_from_Stacks()
queue.queue(10)
queue.queue(100)
queue.queue(1000)
queue.queue(10000)
queue.queue(100000)

print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print('---')

queue.queue(10)
queue.queue(100)
print(queue.dequeue())
print('---')

queue.queue(10000)
queue.queue(1000000)

print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print('---')