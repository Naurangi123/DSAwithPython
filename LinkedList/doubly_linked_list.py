class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

class Linked_list:
    def __init__(self):
        self.head=None

    def createList(self,arr):
        start=self.head
        n=len(arr)

        temp=start
        i=0

        while(i<n):
            newNode=Node(arr[i])
            if(i==0):
                start=newNode
                temp=start
            else:
                temp.next=newNode
                newNode.prev=temp
                temp=temp.next
            i+=1
        self.head=start
        return start
    
    def printList(self):
        temp=self.head
        linked_list=''
        while(temp):
            linked_list+=(str(temp.data)+" ")
            temp=temp.next
        print(linked_list)


arr=[1,2,3,4,5,6,7,8,9]
llist=Linked_list()

llist.createList(arr)
llist.printList()