class Node(object):
      def __init__(self, value):
          self.value=value
          self.next=None
          self.prev=None
          
class List(object):
    def __init__(self):
        self.head=None
        self.tail=None

    def insert(self,n,x):
        #x being the new node, and n being the one before
        #Not actually perfect: how do we append to an existing list?
        if n!=None:
            #If there is an element before the n
            x.next=n.next
            n.next=x
            x.prev=n
            if x.next!=None:
                x.next.prev=x
                
        if self.head==None:
            #empty list adding x, which is both the head and tail
            self.head=self.tail=x
            x.prev=x.next=None
            
        elif self.tail==n:
            #if "x.next!=None" in if above
            #sets the tail to x
            self.tail=x

# ------------------------------------------------

    def delete(self, x):
        active = self.head
 
        while active is not None:
            if active.value == x:
                if active.prev is not None:
                    active.prev.next = active.next
                    if self.tail == active:
                          active.prev.next = None
                          # If the node is the last element
                    else:
                          active.next.prev = active.prev
                    # If the node isn't the first element.
                    
                else:
                    self.head = active.next
                    active.next.prev = None
                    # If node is the first element.
 
            active = active.next

# ------------------------------------------------

    def display(self):
        values=[]
        n=self.head
        while n!=None:
            values.append(str(n.value))
            n=n.next
        print ("List: ",",".join(values))
         
if __name__ == '__main__':
    l=List()
    l.insert(None, Node(4))
    l.insert(l.head,Node(6))
    l.insert(l.head,Node(8))
    l.insert(l.tail,Node(9))
    l.insert(l.tail,Node(11))
    l.insert(l.tail,Node(12))
    l.insert(l.tail,Node(14))
    l.display()
    l.delete(4)
    l.delete(8)
    l.delete(14)
    l.display()


