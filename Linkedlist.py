# A single node of a singly linked list
class Node:
  # constructor
  def __init__(self, data = None, next=None): 
    self.data = data
    self.next = next

# A Linked List class with a single head node
class LinkedList:
  def __init__(self):  
    self.head = None
  
  # insertion method for the linked list
  def insert(self, data):
    newNode = Node(data)
    if(self.head):
      current = self.head
      while(current.next):
        current = current.next
      current.next = newNode
    else:
      self.head = newNode
  
  # print method for the linked list
  def printLL(self):
    current = self.head
    while(current):
      print(current.data)
      current = current.next

# Singly Linked List with insertion and print methods
LL = LinkedList()
LL.insert(3)
LL.insert(4)
LL.insert(5)
LL.printLL()
=================================================================================================
#MY CODE OF LINKEDLIST WITH AMMULY'S============
'''class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class LinkedList:
    def __init__(self):
        self.head=None
    def printLL(self,data):
        n=self.head
        while self.ref is not None:
            print(self.data)
            n=n.ref
LL1=LinkedList()
LL1.data(10)
print(LL1)'''


'''
class Node:
    def __init__(self, data):
        self.data=data
        self.ref=None
class LinkedList:
      def __init__(self):
            self.head=None#this means ll is empty.
      def print_LL(self):
        if self.head is None:
          print("LL is empty") 
        else:
              n=self.head
              while n is not None:
                    print(n.data)
                    n=n.ref
LL1=LinkedList()
LL1.print_LL(self):


'''

    # A single node of a singly linked list
class Node:
  # constructor
  def __init__(self, data = None): 
    self.data = data
    self.ref=None

# A Linked List class with a single head node
class LinkedList:
  def __init__(self):  
    self.head = None
  
  # insertion method for the linked list
  def insert(self, data):
    newNode = Node(data)
    if(self.head):
      current = self.head
      while(current.ref):
        current = current.ref
      current.ref = newNode
    else:
      self.head = newNode
  
  # print method for the linked list
  def printLL(self):
    current = self.head
    while(current):
      print(current.data)
      current = current.ref

# Singly Linked List with insertion and print methods
LL = LinkedList()
LL.insert(3)
LL.insert(4)
LL.insert(5)
LL.printLL()
p1=Node()

print(id(LL.insert(3)))
print(p1.self.ref)
  
