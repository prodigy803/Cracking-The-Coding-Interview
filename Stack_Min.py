## Implement a stack that returns a min value, in addition to pop and append
## All the functions (min, pop and append) should have O(1)

## Stack is Last in First out

## basic idea for problem is that we have to maintain two data-structures
## 1. Main Stack that sort of keeps the data as is
## 2. A min stack that sort of tracks the history of the lowest added numbers in the stack
#### for eg: if the elements added are 2 -> 1 -> 5
#### The min stack will be like 2 -> 1 -> 1

## Everytime we pop the main stack, we have to pop the min-stack and thus we will have the top history too

class Node:
    def __init__(self,value=0):
        self.value = value
        self.next = None
        self.previous = None

# This is maintaining the time-stamp of the min-elements added.
class Min_Stack:
    def __init__(self):
        
        self.tail = None

    def push(self,value):
        
        if self.tail == None:
            temp_node = Node(value)
            self.tail = temp_node

        if value < self.tail.value:
            temp_node = Node(value)
            
            self.tail.next = temp_node

            temp_node.previous = self.tail

            self.tail = temp_node

        else:
            ## Create the same code for tail value
            value = self.tail.value
            
            temp_node = Node(value)
            
            self.tail.next = temp_node

            temp_node.previous = self.tail

            self.tail = temp_node

    def peek(self):

        return self.tail.value

    def pop(self):
        
        self.tail = self.tail.previous
        
        self.tail.next = None
    
class Stack:
    def __init__(self,length=10):

        self.length = length
        self.current_length = 0

        self.tail = None

        self.min_stack = Min_Stack()

    def push(self,value):

        temp_node = Node(value)

        if self.current_length < self.length:
            
            if self.tail == None:
                self.tail = temp_node
                
            else:
                self.tail.next = temp_node
                
                temp_node.previous = self.tail

                self.tail = temp_node
            
            self.min_stack.push(temp_node.value)

            self.current_length +=1
        
        else:
            
            print('stack is already full')

    def pop(self):

        to_be_returned = self.tail.value
        
        self.tail = self.tail.previous
        
        self.tail.next = None

        self.min_stack.pop()

        return to_be_returned

    def min(self):

        return self.min_stack.peek()


min_stack1 = Stack()

min_stack1.push(10)
min_stack1.push(20)
min_stack1.push(30)
min_stack1.push(40)
min_stack1.push(5)
min_stack1.push(10)
min_stack1.push(1)

print(min_stack1.min())

min_stack1.pop()

print(min_stack1.min())

min_stack1.pop()
min_stack1.pop()

print(min_stack1.min())

## Output:
# 1
# 5
# 10

