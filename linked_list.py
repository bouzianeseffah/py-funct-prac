class Node:
  def __init__(self, data, reference = None):
    self.data = data
    self.reference = reference


class LinkedList:
  def __init__(self, head = None):
    self.head = head
    self.last_node = None


  def print_linked_list(self):
    if self.head is None:
      print('the linked list is empty ')
    else:
      c_node = self.head
      while c_node is not None:
        print(c_node.data)
        c_node = c_node.reference 
  def add_to_start(self, data):
    n_node = Node(data)
    n_node.reference = self.head
    self.head = n_node
  def append(self, data):
    if self.last_node is None:
      self.head = Node(data)
      self.last_node = self.head
    else:
      self.last_node.reference = Node(data)
      self.last_node = self.last_node.reference
  def display(self):
    current = self.head
    while current is not None:
      print(current.data)
      current = current.reference 
    print()     








L = LinkedList()
L.append(1)
L.append(2)
L.append(3)
L.display()



"""LinkedList1 = LinkedList()
LinkedList1.add_to_start(82)
LinkedList1.add_to_start(15)
LinkedList1.add_to_start(85)
LinkedList1.print_linked_list()"""
"""node1 = Node(5)
node2 = Node(11)
node1.reference = node2
print(node1.reference)"""




    
