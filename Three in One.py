## Describe how you could use a singly array to implement three stacks

## Stack is Last in First Out.

class Node:
    
    def __init__(self, value = 0):
        self.value = value

class three_stacks_array:
    # array in this case we will consider as a list []

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
        
