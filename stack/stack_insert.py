class Stack: 
    def __init__(self) -> None:
        self.st = []

    def isempty(self):
        return self.st == []
    
    def push(self, element):
        self.st.append(element)

    def pop(self):
        if self.isempty():
            return -1
        else:
            return self.st.pop()
    def peep(self):
        if self.isempty():
            return -1
        else:
            return self.st[-1]

    def search(self, element):
        if self.isempty():
            return -1
        else:
            try:
                n = self.st.index(element)
                return len(self.st) - n
            except ValueError:
                return -2

    def display(self):
        return self.st
    
stk = Stack()
print(stk.isempty())
print(stk.push([1, 2, 3, 4, 5, 6, 7, 8]))
print(stk.pop())
print(stk.peep())
print(stk.search(3))
print(stk.display())
