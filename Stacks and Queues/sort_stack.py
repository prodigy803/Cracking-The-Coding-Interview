"""
Problem Statement:
Write a program to sort a stack such that the smallest items are on the top. You can use an additional temp_stack but you
may note copy the elements into any other data structures (such as an array). The stack supports the following opertions:
push, pop, peek and isEmpty.

Solution:
We will use a temp_stack which will contain the bigger elements incase a smaller number is pushed in the stack.
for eg. consider a stack where 10 is at the top and 4 is at the bottom like:
    10 - 9 - 7 - 5 - 4

now say we enter 6 in the stack:
    step 1: compare 6 with top of stack ie 10, if its smaller, pop main stack and keep that detail in temp_stack
        - main stack - 9 - 7 - 5 - 4
        - temp stack - 10
    
    step 2: compare 6 with top of stack ie 9, if its smaller, pop main stack and keep that detail in temp_stack
        - main stack - 7 - 5 - 4
        - temp stack - 9 - 10

    step 3: compare 6 with top of stack ie 7, if its smaller, pop main stack and keep that detail in temp_stack
        - main stack - 5 - 4
        - temp stack - 7 - 9 - 10

    step 4: compare 6 with top of stack ie 5, if its bigger, push 6 in main stack main stack and keep that detail in temp_stack
        - main stack - 6 - 5 - 4
        - temp stack - 7 - 9 - 10

    step 5: Once that element has been added, we can pop off elements of temp_stack one by one and push them in main_stack.
        - main stack - 6 - 5 - 4
        - temp stack - 7 - 9 - 10
"""


class Node:

    def __init__(self, value = 0):
        self.value = value
        self.next = None
        self.previous = None

class Stack:

    def __init__(self):

        self.tail = None
        self.length = 0

    def push(self, value):
        temp_node = Node(value)

        if self.tail == None:
            self.tail = temp_node
        
        else:
            self.tail.next = temp_node
            temp_node.previous = self.tail
            self.tail = temp_node

        self.length += 1

    def pop(self):
        value_to_be_returned = self.tail.value

        if self.tail.previous != None:
            self.tail = self.tail.previous
            self.tail.next = None
        else:
            self.tail = None
        

        self.length -= 1

        return value_to_be_returned

    def peek(self):
        return self.tail.value

    def isEmpty(self):
        return self.length == 0

    def print_all(self):
        
        while self.tail.previous != None:
            print(self.tail.value)
            if self.tail.previous == None:
                self.tail = None
                break
            self.tail = self.tail.previous



class sorted_Stack:

    def __init__(self):

        self.tail = None
        self.length = 0
        

    def push(self, value):
        temp_node = Node(value)

        if self.tail == None:
            self.tail = temp_node
            self.length +=1

        else:
            # Here we are just checking if value is greater than the first tail of the main stack
            # if it is, just push the element on top of the main_stack
            if self.tail.value < value:
                self.tail.next = temp_node
                temp_node.previous = self.tail
                self.tail = temp_node

            else:

                # Here we are dealing with the scenario that the element has to be pushed in the middle of the stack

                temp_stack = Stack()

                # we are ensuring that we arent doing any checks on a null stack
                while self.tail != None:
                    if self.tail.value > value:
                        temp_stack.push(self.tail.value)
                    
                    elif self.tail.value < value:
                        break
                    self.tail = self.tail.previous
                    self.length -=1

                # If we did iterate through to the end of the stack, just set the element as the tail

                if self.tail == None:
                    self.tail = temp_node
                    self.length +=1
                
                # incase we have to enter the element in the middle of the stack, just push it how we would normally do.
                else:
                    self.tail.next = temp_node
                    temp_node.previous = self.tail
                    self.tail = temp_node
                    self.length +=1

                # this step just adds the eleements of the temp_stack back to the main_stack
                while temp_stack.length > 0:
                    temp_node_2 = Node(temp_stack.pop())
                    self.tail.next = temp_node_2
                    temp_node_2.previous = self.tail
                    self.tail = temp_node_2
                    self.length +=1

    def pop(self):
        value_to_be_returned = self.tail.value

        if self.tail.previous != None:
            self.tail = self.tail.previous
            self.tail.next = None
        else:
            self.tail = None
        

        self.length -= 1

        return value_to_be_returned

    def peek(self):
        return self.tail.value

    def isEmpty(self):
        return self.length == 0




stack = sorted_Stack()

stack.push(9)

stack.push(7)

stack.push(125)

stack.push(10)

stack.push(8)

stack.push(120)

stack.push(150)

stack.push(140)

stack.push(1)

print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())

"""
Output:

150
140
125
120
10
9
8
7
1
"""