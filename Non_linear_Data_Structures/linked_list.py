class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedL:
    def __init__(self):
        self.head=None
    def append(self,data):
        M=Node(data)
        if self.head==None:
            self.head=M
        else:
            temp=self.head
            while(temp.next!=None):
                temp=temp.next
            temp.next=M
    def prepend(self,data):
        M=Node(data)
        if self.head==None:
            self.head=M
        else:
            M.next=self.head
            self.head=M
    def insert(self,data,k):
        M=Node(data)
        if k==0:
            self.prepend(data)
        else:
            temp=self.head
            for i in range(k-1):
                temp=temp.next
            M.next=temp.next
            temp.next=M
    def length(self):
        c=0
        if self.head==None:
            return c
        else:
            temp=self.head
            while(temp!=None):
                temp=temp.next
                c+=1
            return c
    def search(self,value):
        temp=self.head
        while(temp!=None):
            if temp.data==value:
                return "Found"
            else:
                temp=temp.next
        else:
            return "Not Found"
    def middle(self,k=0):
        slow=self.head
        fast=self.head
        prev=None
        while(fast and fast.next):
            prev=slow
            slow=slow.next
            fast=fast.next.next
        if k==0:
            return prev.data
        else:
            return slow.data
        
    def reverse(self):
        prev=None
        cur=self.head
        while cur:
            temp=cur.next
            cur.next=prev
            prev=cur
            cur=temp
        self.head=prev
    def show(self):
        temp=self.head
        while(temp!=None):
            print(temp.data,end="->")
            temp=temp.next

        
a=LinkedL()
a.append(10)
a.prepend(25)
a.append(24)
a.insert(2,3)
print(a.length())
print(a.search(2))
print(a.show())
a.reverse()
print(a.middle(1))
print(a.show())
print(a.middle(1))
a.append(56)
print(a.show())
a.plot()

            




