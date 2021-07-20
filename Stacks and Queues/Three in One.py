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

class Node:
    
    def __init__(self, value = 0):
        self.value = value

class three_stacks_array:
    
    def __init__(self,length=10):

        self.array = [None for x in range(length)]

        splitter = length//3

        self.stacks = []
        
        self.index_at_tops = [-1,-1,-1]
        
        if int(length%3) == 2:
            self.stacks.append(self.array[ : splitter])
        
            self.stacks.append(self.array[ splitter: splitter*2+1])

            self.stacks.append(self.array[ splitter*2+1:])
            
        else:
            self.stacks.append(self.array[ : splitter])

            self.stacks.append(self.array[ splitter: splitter*2])

            self.stacks.append(self.array[splitter*2:])


    def append(self,value,stack_no=0):
        node = Node(value)
        
        if (self.index_at_tops[stack_no] * -1) -1 == len(self.stacks[stack_no]):
            print('stack is full')

        else:
            self.stacks[stack_no][self.index_at_tops[stack_no]] = node

            self.index_at_tops[stack_no] -= 1


    def pop(self,stack_no=0):

        if self.index_at_tops[stack_no] == -1:
            return 'Stack is already empty'
        
        else:
            value_to_be_popped = self.stacks[stack_no][self.index_at_tops[stack_no]+1]

            self.stacks[stack_no][self.index_at_tops[stack_no]+1] = None
            
            self.index_at_tops[stack_no] += 1

        return value_to_be_popped.value


    def peek(self,stack_no=0):

        return self.stacks[stack_no][self.index_at_tops[stack_no]+1].value


    def isEmpty(self, stack_no=1):

        if self.index_at_tops[stack_no] == -1:
            return True

        else:
            return False

    def print_all_values(self,stack_no=0):

        print([x.value for x in self.stacks[stack_no]])

stacks = three_stacks_array(9)


stacks.append(10,stack_no=0)
stacks.append(20,stack_no=0)
stacks.append(30,stack_no=0)

stacks.append(110,stack_no=1)
stacks.append(120,stack_no=1)
stacks.append(130,stack_no=1)


stacks.append(30,stack_no=2)
stacks.append(40,stack_no=2)
stacks.append(50,stack_no=2)


try:
    stacks.append(50,stack_no=3)

except:
    
    print('Opps that stack didnt exist')

stacks.print_all_values(stack_no=0)
stacks.print_all_values(stack_no=1)
stacks.print_all_values(stack_no=2)

print(stacks.pop(stack_no=0))
print(stacks.peek(stack_no=0))

print('----------')

print(stacks.pop(stack_no=0))
print(stacks.peek(stack_no=0))


###---------------###
# Output
###---------------###

# Opps that stack didnt exist
# [30, 20, 10]
# [130, 120, 110]
# [50, 40, 30]
# 30
# 20
# ----------
# 20
# 10