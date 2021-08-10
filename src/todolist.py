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
            print(temp.data)
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

# taskList = MyLinkedList()

# #instructions of how to use this app
# print("Welcome to Todo List, this is a task tracking app.")
# print("Return [POP] to finish the current task located at the beginning of the queue.")
# print("Return [IB, \"task\"] to insert task at beginning of the queue. Example: IB, Lunch")
# print("Return [IE, \"task\"] to insert task at end of the queue. Example: IE, Lunch")
# print("Return [IP, index of position, \"task\"] to insert task at target position. Example: IP, 0, Lunch")
# print("Return [IS, \"target task\", \"task\"] to insert task after target task. Example: IS, Lunch, Dinner")
# print("Return [RA, index to remove] to remove one task from the target index. Example: RA, 0")
# print("Return [RT, \"target task\"] to remove the target task. Example: RS, Lunch")
# print("Return [FIND, index of position] to find the task at the target position. Example: FIND, 0")
# print("Return [SEARCH, \"target task\"] to find the index of the target task name. Example: SEARCH, Lunch")

# while 1:
# 	#TODO
# 	print("")
# 	print("")
# 	print("")
# 	print("Current list size: ", taskList.size)
# 	print("Current task list:")
# 	taskList.printlist()
# 	if taskList.size != 0:
# 		print("Next task to do:")
# 		print(taskList.head.data)
# 	else:
# 		print("The task list is currently empty.")
# 	print("")
# 	print("")
# 	print("")
# 	print("Please enter the command")
# 	stdin = input().split(",")

# 	#Case POP
# 	if stdin[0] == "POP":
# 		temp = taskList.pop()
# 		if temp != -1:
# 			print("******")
# 			print("Task ", temp.data, " is finished.")
# 			print("******")
# 	#Case IB
# 	elif stdin[0] == "IB":
# 		taskList.insert_at_beginning(stdin[1])
# 		print("******")
# 		print("Task ", stdin[1], " is inserted at the beginning of the list.")
# 		print("******")
# 	#Case IE
# 	elif stdin[0] == "IE":
# 		taskList.insert_at_end(stdin[1])
# 		print("******")
# 		print("Task ", stdin[1], " is inserted at the end of the list.")
# 		print("******")
# 	#Case IP
# 	elif stdin[0] == "IP":
# 		temp = taskList.insert_at_pos(int(stdin[1]), stdin[2])
# 		if temp != -1:
# 			print("******")
# 			print("Task ", stdin[2], " is inserted at index ", stdin[1], " .")
# 			print("******")
# 	#Case IS
# 	elif stdin[0] == "IS":
# 		temp = taskList.insert_after_target_value(stdin[1], stdin[2])
# 		if temp != -1:
# 			print("******")
# 			print("Task ", stdin[2], " is inserted after task ", stdin[1], " .")
# 			print("******")
# 	#Case RA
# 	elif stdin[0] == "RA":
# 		temp = taskList.remove_at(int(stdin[1]))
# 		if temp != -1:
# 			print("******")
# 			print("Task ", temp.data, " located at index ", stdin[1], " is removed.")
# 			print("******")
# 	#Case RT
# 	elif stdin[0] == "RT":
# 		temp = taskList.remove_target_value(stdin[1])
# 		if temp != -1:
# 			print("******")
# 			print("Task ", stdin[1], " is removed.")
# 			print("******")
# 	#Case FIND
# 	elif stdin[0] == "FIND":
# 		temp = taskList.node_at(int(stdin[1]))
# 		if temp != -1:
# 			print("******")
# 			print("Task ", temp.data, " is found at index ", stdin[1], " .")
# 			print("******")
# 	#Case SEARCH
# 	elif stdin[0] == "SEARCH":
# 		temp = taskList.index_of(stdin[1])
# 		if temp != -1:
# 			print("******")
# 			print("Task ", stdin[1], " is found at index ", temp, " .")
# 			print("******")
# 	else:
# 		print("******")
# 		print("Error: Command is not valid.")
# 		print("******")
