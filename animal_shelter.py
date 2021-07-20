"""
Problem Statement:
An animal shelter holds only doggos and cattos, operates on a first in first out basis. An adoptor can either request a Cat or a Dog (and they will
receive the oldest from that particular category) or they can request any with them receiving the oldest animal currently present.

Solution: Simple, have a time-stamp variable in the common_animals queue interface and add that time-stamp while creating the individual animal nodes in the specific animal queue:

"""



class animal_node():

    def __init__(self, animal_type = 'catto', time_stamp = 0):
        self.next = None
        self.previous = None
        self.animal_type = animal_type
        self.time_stamp = time_stamp

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def queue(self, animal_type = 'catto', time_stamp = 0):
        temp_animal = animal_node(animal_type = animal_type,time_stamp = time_stamp)

        if self.head == None:
            self.head = self.tail = temp_animal

        else:
            
            self.tail.next = temp_animal
            temp_animal.previous = self.tail
            self.tail = temp_animal
        
        self.length +=1

    def dequeue(self):
        value_to_be_returned, animal_type= self.head.time_stamp, self.head.animal_type

        if self.head != None:

            if self.head.next != None:

                self.head = self.head.next
            else:
                self.head = self.tail = None
            self.length -=1

            return value_to_be_returned, animal_type

        else:

            return "Queue is empty"
        
    def peek_time(self):
        return self.head.time_stamp

class animals_queue:
    def __init__(self):
        self.catto_stack = Queue()
        self.doggo_stack = Queue()
        self.timer = 0
        
    def queue(self,animal_type = 'catto'):
        self.timer +=1
        if animal_type == 'catto':
            self.catto_stack.queue(animal_type = animal_type,time_stamp = self.timer)

        elif animal_type == 'doggo':
            self.doggo_stack.queue(animal_type = animal_type,time_stamp = self.timer)

        else:
            print('Only cattos and doggos please')

    def dequeue(self):
        if (self.catto_stack.length > 0) and (self.doggo_stack.length > 0):
            if self.catto_stack.peek_time() < self.doggo_stack.peek_time(): 
                return self.catto_stack.dequeue()
            else:
                return self.doggo_stack.dequeue()

        elif (self.doggo_stack.length > 0) and (self.catto_stack.length == 0):
            return self.doggo_stack.dequeue()

        elif (self.doggo_stack.length == 0) and (self.catto_stack.length > 0):
            return self.catto_stack.dequeue()

    def dequeueCatto(self):
        if (self.catto_stack.length > 0):
            return self.catto_stack.dequeue()

        else:
            return "Cattos are all gone :)"

    def dequeueDoggo(self):
        if (self.doggo_stack.length > 0):
            return self.doggo_stack.dequeue()

        else:
            return "doggos are all gone :)"


animals_to_be_adopted = animals_queue()

animals_to_be_adopted.queue('catto')
animals_to_be_adopted.queue('catto')
animals_to_be_adopted.queue('catto')
animals_to_be_adopted.queue('doggo')
animals_to_be_adopted.queue('doggo')
animals_to_be_adopted.queue('doggo')
animals_to_be_adopted.queue('doggo')
animals_to_be_adopted.queue('doggo')
animals_to_be_adopted.queue('catto')
animals_to_be_adopted.queue('catto')
animals_to_be_adopted.queue('doggo')

print(animals_to_be_adopted.dequeue())
print(animals_to_be_adopted.dequeue())
print(animals_to_be_adopted.dequeue())
print(animals_to_be_adopted.dequeue())
print(animals_to_be_adopted.dequeue())
print(animals_to_be_adopted.dequeue())
print(animals_to_be_adopted.dequeue())
print(animals_to_be_adopted.dequeue())
print(animals_to_be_adopted.dequeue())
print('----')
print(animals_to_be_adopted.dequeueDoggo())
print(animals_to_be_adopted.dequeueCatto())
print(animals_to_be_adopted.dequeueDoggo())
print(animals_to_be_adopted.dequeueCatto())

animals_to_be_adopted.queue('catto')
animals_to_be_adopted.queue('catto')
animals_to_be_adopted.queue('catto')
animals_to_be_adopted.queue('doggo')
animals_to_be_adopted.queue('doggo')
animals_to_be_adopted.queue('doggo')
animals_to_be_adopted.queue('doggo')
animals_to_be_adopted.queue('doggo')
animals_to_be_adopted.queue('catto')
animals_to_be_adopted.queue('catto')
animals_to_be_adopted.queue('doggo')

print('----')

print(animals_to_be_adopted.dequeueDoggo())
print(animals_to_be_adopted.dequeueCatto())
print(animals_to_be_adopted.dequeueDoggo())
print(animals_to_be_adopted.dequeueCatto())
print(animals_to_be_adopted.dequeue())
print(animals_to_be_adopted.dequeue())
