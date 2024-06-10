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
    def show(self):
        temp=self.head
        while(temp!=None):
            print(temp.data,end="->")
            temp=temp.next
def merger(a,b):
    z=LinkedL()
    temp1=a
    temp2=b
    while(temp1 and temp2):
        if temp1.data<temp2.data:
            z.append(temp1.data)
            temp1=temp1.next
        else:
            z.append(temp2.data)
            temp2=temp2.next
    while(temp1):
        z.append(temp1.data)
        temp1=temp1.next
    while(temp2):
        z.append(temp2.data)
        temp2=temp2.next
    return z
a=LinkedL()
a.append(10)
a.append(11)
a.append(21)
a.append(24)
a.append(29)
print(a.show())
b=LinkedL()
b.append(7)
b.append(14)
b.append(20)
b.append(20)
b.append(23)
b.append(30)
b.append(49)
print(b.show())
p=merger(a.head,b.head)
print(p.show())


    