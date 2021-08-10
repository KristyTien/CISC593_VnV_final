class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    # method used to print out the whole list
    def printlist(self):
        counter = 0
        temp = self.head
        while temp is not None:
            print(counter, temp.data)
            counter += 1
            temp = temp.next

    # method used to insert a node at begining
    def insert_at_beginning(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
        self.size += 1

    # method used to insert a node at end
    def insert_at_end(self, data):
        if self.size == 0:
            self.insert_at_beginning(data)
        else:
            newNode = Node(data)
            lastNode = self.head
            while lastNode.next is not None:
                lastNode = lastNode.next
            lastNode.next = newNode
            self.size += 1

    # method used to insert a node at a given index position
    def insert_at_pos(self, pos, data):
        if pos > self.size:
            print("Error: Position index lager than size of list.")
            return -1
        elif pos == 0:
            newNode = Node(data)
            newNode.next = self.head
            self.head = newNode
            self.size += 1
            return 0
        else:
            counter = pos - 1
            temp = self.head.next
            before_temp = self.head
            while counter is not 0:
                temp = temp.next
                before_temp = before_temp.next
                counter -= 1
            newNode = Node(data)
            newNode.next = temp
            before_temp.next = newNode
            self.size += 1
            return 0

    # method used to insert a node after a specefic node
    def insert_after_target_value(self, target, data):
        if target is None:
            print("Error: Target value is None.")
            return -1
        else:
            temp = self.head
            while temp is not None:
                if temp.data == target:
                    break
                else:
                    temp = temp.next
            if temp is None:
                print("Error: Target value not found in list.")
                return -1
            else:
                newNode = Node(data)
                newNode.next = temp.next
                temp.next = newNode
                self.size += 1
                return 0

    # method used to pop the head node
    def pop(self):
        if self.size == 0:
            print("Error: Cannot pop from an empty list.")
            return -1
        else:
            temp = self.head
            self.head = self.head.next
            self.size -= 1
            # print(temp.data)
            return temp

    # method used to remove a node at given index position
    def remove_at(self, pos):
        if pos + 1 > self.size:
            print("Error: Index not valid.")
            return None
        elif pos == 0:
            return self.pop()
        else:
            counter = pos - 1
            before_remove = self.head
            while counter is not 0:
                before_remove = before_remove.next
                counter -= 1
            temp = before_remove.next
            before_remove.next = before_remove.next.next
            self.size -= 1
            return temp

    # method used to remove a node with specefic data value
    def remove_target_value(self, target):
        if target is None:
            print("Error: Target value is None.")
            return -1
        else:
            pos = self.index_of(target)
            if pos == -1:
                return -1
            else:
                self.remove_at(pos)

    # method used to get the node at given index position
    def node_at(self, pos):
        if pos + 1 > self.size:
            print("Error: Index not valid.")
            return -1
        else:
            counter = pos
            temp = self.head
            while counter is not 0:
                temp = temp.next
                counter -= 1
            return temp

    # method used to get the index of a given node data value
    def index_of(self, data):
        if data is None:
            print("Error: Target value is None.")
            return -1
        else:
            pos = 0
            temp = self.head
            while temp is not None:
                if temp.data == data:
                    break
                else:
                    temp = temp.next
                    pos += 1
            if temp is None:
                print("Error: Target value not found in list.")
                return -1
            else:
                return pos