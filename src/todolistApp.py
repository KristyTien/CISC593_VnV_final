import sys;
sys.path.append('../src') 
import todolist

class TodolistApp:
    def __init__(self):
        self.todolist = todolist.LinkedList()
        self.running = True

    def printGreet(self):
        print("Welcome to Todo List, this is a task tracking app.")
        print(
            "Return [POP] to finish the current task located at the beginning of the queue.")
        print(
            "Return [IB, \"task\"] to insert task at beginning of the queue. Example: IB, Lunch")
        print(
            "Return [IE, \"task\"] to insert task at end of the queue. Example: IE, Lunch")
        print(
            "Return [IP, index of position, \"task\"] to insert task at target position. Example: IP, 0, Lunch")
        print(
            "Return [IS, \"target task\", \"task\"] to insert task after target task. Example: IS, Lunch, Dinner")
        print(
            "Return [RA, index to remove] to remove one task from the target index. Example: RA, 0")
        print(
            "Return [RT, \"target task\"] to remove the target task. Example: RS, Lunch")
        print(
            "Return [FIND, index of position] to find the task at the target position. Example: FIND, 0")
        print(
            "Return [SEARCH, \"target task\"] to find the index of the target task name. Example: SEARCH, Lunch")
        print(
            "Return [QUIT] to end the app")

    def start(self):
        self.printGreet()
        while(self.running):
            stdin = input("Please enter the command\n").split(",")
            self.takeCommand(*stdin)

    def takeCommand(self, action, content1="", content2=""):
        #Case POP
        if action == "POP":
            temp = self.todolist.pop()
            if temp != -1:
                print("******")
                print("Task ", temp.data, " is finished.")
                print("******")
        #Case IB
        elif action == "IB":
            self.todolist.insert_at_beginning(content1)
            print("******")
            print("Task ", content1, " is inserted at the beginning of the list.")
            print("******")
        #Case IE
        elif action == "IE":
            self.todolist.insert_at_end(content1)
            print("******")
            print("Task ", content1, " is inserted at the end of the list.")
            print("******")
        #Case IP
        elif action == "IP":
            temp = self.todolist.insert_at_pos(int(content1), content2)
            if temp != -1:
                print("******")
                print("Task ", content2, " is inserted at index ", content1, " .")
                print("******")
        #Case IS
        elif action == "IS":
            temp = self.todolist.insert_after_target_value(content1, content2)
            if temp != -1:
                print("******")
                print("Task ", content2, " is inserted after task ", content1, " .")
                print("******")
        #Case RA
        elif action == "RA":
            temp = self.todolist.remove_at(int(content1))
            if temp != -1:
                print("******")
                print("Task ", temp.data, " located at index ", content1, " is removed.")
                print("******")
        #Case RT
        elif action == "RT":
            temp = self.todolist.remove_target_value(content1)
            if temp != -1:
                print("******")
                print("Task ", content1, " is removed.")
                print("******")
        #Case FIND
        elif action == "FIND":
            temp = self.todolist.node_at(int(content1))
            if temp != -1:
                print("******")
                print("Task ", temp.data, " is found at index ", content1, " .")
                print("******")
        #Case SEARCH
        elif action == "SEARCH":
            temp = self.todolist.index_of(content1)
            if temp != -1:
                print("******")
                print("Task ", content1, " is found at index ", temp, " .")
                print("******")
        elif action == "QUIT":
            print("*****")
            self.running = False
            print("App Ended.")
        else:
            print("******")
            print("Error: Command is not valid.")
            print("******")


if __name__ == "__main__":  
    app = TodolistApp()
    app.start()

