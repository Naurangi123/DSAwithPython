
class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.next=None

class LinkedList:

    def __init__(self) -> None:
        self.head=None

    def printlist(self):
        temp=self.head
        linked_list=""
        while(temp):
            linked_list+=(str(temp.data)+" ")
            temp=temp.next
        print(linked_list)

    def insertNode(self,val,pos):
        target=Node(val)
        if(pos==0):
            target.next=self.head
            self.head=target
            return
        
        def getPrev(pos):
            temp=self.head
            count=1
            while(count<pos):
                temp=temp.next
                count+=1
            return temp


        prev=getPrev(pos)
        nextNode=prev.next

        prev.next=target
        target.next=nextNode


linked_list=LinkedList()
linked_list.head=Node(5)

second_node=Node(1)
third_node=Node(6)
fourth_node=Node(8)


linked_list.head.next=second_node
second_node.next=third_node
third_node.next=fourth_node


#Insertion Operation

linked_list.insertNode(9,3)
linked_list.printlist()