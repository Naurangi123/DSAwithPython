class QueueLine:
    def __init__(self):
        self.q=[]


    # Adding elements one-by-one into Queue
    def enqueue(self,x):
        self.q.append(x)
    
    def dequeue(self):
        if(len(self.q)>0):
            self.q.pop(0)
    # To check front queue element in the Queue
    def front(self):
        if(len(self.q)==0):
            return None
        return self.q[0]
    # Print the Queue
    def printQueue(self):
        for x in self.q:
            print(x)
    # Adding multiple elements only one time into the Queue
    def adding_elements(self,elements):
        for element in elements:
            self.enqueue(element)

        
    

q=QueueLine()

add_enqueue=[1,3,4,6,7,9]
q.adding_elements(add_enqueue)

q.printQueue()
    






