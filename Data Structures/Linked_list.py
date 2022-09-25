class Node:
    def __init__(self, datavalue = None):
        self.datavalue = datavalue
        self.nextvalue = None

class SLinkedList:
    def __init__(self):
        self.headvalue = None


list1 = SLinkedList()
list1.headvalue = Node("Monday")
Node2 = Node("Tuesday")
Node3 = Node("Wednesday")

#Link first Node to second node
list1.headvalue.nextvalue = Node2

#Link second Node to third node
Node2.nextvalue = Node3

#References
# https://www.tutorialspoint.com/python_data_structure/python_linked_lists.htm
