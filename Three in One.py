## Describe how you could use a singly array to implement three stacks

## Stack is Last in First Out.

## Basic logic of the code is that we take an array (in our case we will be taking a list)

## Once we get the size of the array, we will split the array into three partitions
## If the size is 8, sizes will be 3,3,2
## if the size is 7, sizes will be 3,2,2
## We are also tracking the tail of the arrays since we are working with the LIFO logic

## Class Node:
## We are only tracking the value, and the class three-stacks-array is tracking the individual stacks and the their tails

## Class three_stacks_array:
## Here we are initializing the array and creating the individual "stacks"
## We are then initializing the individual stacks as self.stacks.
## We are then tracking the tails or tops as self.index_at_tops

## While appending, we are shifting the value by one and changing the counter of index_at_tops to reflect the last in value

## While popping, we are popping the value at self.index_at_tops and setting the top as None in case its the last element.

W

class Node:
    
    def __init__(self, value = 0):
        self.value = value

class three_stacks_array:
    
    def __init__(self,length=10):

        self.array = [None for x in range(length)]

        splitter = int(length / 3)

        self.stacks = []
        self.index_at_tops = []

        if int(length%3) == 2:
            self.stacks.append(self.array[ : splitter+1])
            self.index_at_tops.append(-1)
        
            self.stacks.append(self.array[ splitter+1: splitter*2+1])
            self.index_at_tops.append(-1)

            self.stacks.append(self.array[ splitter*2+1:])
            self.index_at_tops.append(-1)

        else:
                
            self.stacks.append(self.array[ : splitter])
            self.index_at_tops.append(-1)

            self.stacks.append(self.array[ splitter: splitter*2])
            self.index_at_tops.append(-1)

            self.stacks.append(self.array[ splitter*2:])
            self.index_at_tops.append(-1)

        print(self.stacks)

    def append(self,value,stack_no=0):

        node = Node(value)
        
        if self.index_at_tops[stack_no] * -1 == len(self.stacks[stack_no]):
            print('stack is full')
        else:
            self.stacks[self.index_at_tops[stack_no]] == node
            self.index_at_tops[stack_no] -=1

    def pop(self,stack_no=0):
        value_to_be_popped = self.stacks[stack_no][self.index_at_tops[stack_no]]

        if self.index_at_tops[stack_no] == -2:

            self.stacks[stack_no][self.index_at_tops[stack_no]] = None
            self.index_at_tops[stack_no] -= 1

        else:
            self.stacks[stack_no][self.index_at_tops[stack_no]] = self.stacks[stack_no][self.index_at_tops[stack_no]-1]
            self.index_at_tops[stack_no] += 1

        return value_to_be_popped 

    def peek(self,stack_no=0):

        return self.stacks[stack_no][self.index_at_tops[stack_no]]

    def isEmpty(self, stack_no=1):
        
        if self.index_at_tops[stack_no] == -1:
            return True
        else:
            return False
        
