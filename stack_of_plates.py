## Problem Statement:

"""
Imagine a (literal) stack of plates. If the stack gets too hight, it might topple.Therefor, in real life, we would likely start a new stack 
when the preious stack exceeds some threshold. Implement a data structure "SetOfStacks" that mimics this. SetOfStacks should be composed of several
stacks and should create a new stack once the previous exceeds capacity. SetOfStacks.push() and SetOfStacks.pop() should behave identically to a 
single stack (ie. Pop should return the same value as if it were a single stack)
"""

## Since its sort of a dynamic allocation problem, we will assume that the length of stacks shall be 10

## This solution sort of maintains a list of stacks that are added. We can substitute that with a stack of stacks but that would 
## increase the codelines. The idea would be the same but we would be implementing three classes, single_stack, stack_of_stacks and 
## set of stacks that sort of manipulates the stack_of_stacks. To reduce that I have used a list and overall understanding of the text


class Node:

    def __init__(self,value=0):
        self.value = value
        self.next = None
        self.previous = None

    

class Single_Stack:

    def __init__(self, length = 10):
        self.length = length
        self.tail = None
        self.current_length = 0

    def push(self,value=0):
        
        temp_node = Node(value)

        if self.tail == None:
            self.tail = temp_node

        else:
            
            self.tail.next = temp_node
            temp_node.previous = self.tail
            self.tail = temp_node

        self.current_length +=1

    def pop(self):
        value_to_be_returned = self.tail.value

        if self.tail.previous != None:
            self.tail = self.tail.previous
            self.tail.next = None
        
        else:
            self.tail = None
        
        self.current_length -=1
        
        return value_to_be_returned

class SetOfStacks:
    def __init__(self):
        self.stacks = []
        self.tracker_of_stacks = 0

    def push(self,value=0):

        temp_node = Node(value)

        if len(self.stacks) == 0:
            self.stacks.append(Single_Stack())
            self.stacks[self.tracker_of_stacks].push(temp_node)

        else:

            if self.stacks[self.tracker_of_stacks].current_length < 10:

                self.stacks[self.tracker_of_stacks].push(temp_node)

            else:

                self.tracker_of_stacks +=1
                self.stacks.append(Single_Stack())
                self.stacks[self.tracker_of_stacks].push(temp_node)

    def pop(self):
        if len(self.stacks) == 0:
            value_to_be_returned = 'Stack of Stacks is empty'
        else:

            len_of_top_stack = self.stacks[self.tracker_of_stacks].current_length 

            if len_of_top_stack == 1:
                value_to_be_returned = self.stacks[self.tracker_of_stacks].pop().value
                self.tracker_of_stacks -=1
                self.stacks.pop()

            else:

                value_to_be_returned = self.stacks[self.tracker_of_stacks].pop().value

        return value_to_be_returned

SS = SetOfStacks()

SS.push(10)
SS.push(1)
SS.push(100)
SS.push(111)
SS.push(2)
SS.push(4)
SS.push(3)
SS.push(10000)
SS.push(12)
SS.push(15)
SS.push(19)
SS.push(22)
SS.push(26)
SS.push(10)
SS.push(1)
SS.push(100)
SS.push(111)
SS.push(2)
SS.push(4)
SS.push(3)
SS.push(10000)
SS.push(12)
SS.push(15)
SS.push(19)
SS.push(22)
SS.push(26)

print(SS.pop())
print(SS.pop())
print(SS.pop())
print(SS.pop())
print(SS.pop())
print(SS.pop())
print(SS.pop())
print(SS.pop())
print(SS.pop())
print(SS.pop())
print(SS.pop())
print(SS.pop())
print(SS.pop())
print(SS.pop())
print(SS.pop())
print(SS.pop())
print(SS.pop())
print(SS.pop())
print(SS.pop())
print(SS.pop())
print(SS.pop())
print(SS.pop())
print(SS.pop())
print(SS.pop())
print(SS.pop())
print(SS.pop())
print(SS.pop())
print(SS.pop())


"""
Output:
26
22
19
15
12
10000
3
4
2
111
100
1
10
26
22
19
15
12
10000
3
4
2
111
100
1
10
Stack of Stacks is empty
Stack of Stacks is empty
"""