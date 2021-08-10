import unittest
import sys
import io 

sys.path.append('../src') 
import todolist

class TestTodolist(unittest.TestCase):
    def getEnd(self, head):
        tmp = head
        while(tmp.next is not None):            
            tmp = tmp.next
        return tmp

    def test_node(self):
        listHead = todolist.Node("task1")
        listHead.next = todolist.Node("task2")

        self.assertEqual(listHead.data, "task1")
        self.assertEqual(listHead.next.data, "task2")

    def test_linkedList(self):
        list = todolist.LinkedList()

        self.assertIsNone(list.head)
        self.assertEqual(list.size, 0)
    
    def test_printlist(self):
        capturedOutput = io.StringIO()               # Create StringIO object
        sys.stdout = capturedOutput                   #  and redirect stdout.
        testList = todolist.LinkedList()
        testList.insert_at_beginning("head")
        testList.insert_at_end("end")
        testList.printlist()
        self.assertTrue("0 head" in capturedOutput.getvalue())
        self.assertTrue("1 end" in capturedOutput.getvalue())
        sys.stdout = sys.__stdout__

    def test_insertAtBeginning(self):
        testTask1 = "testTask1"
        testTask2 = "testTask2"
        testList = todolist.LinkedList()
        testList.insert_at_beginning(testTask1)
        self.assertEqual(testList.head.data, testTask1)
        testList.insert_at_beginning(testTask2)
        self.assertEqual(testList.head.data, testTask2)
    
    def test_insertAtEnd_0(self):
        testTask1 = "testTask1"
        testList = todolist.LinkedList()
        testList.insert_at_end(testTask1)
        self.assertEqual(testList.head.data, "testTask1")
    
    def test_insertAtEnd(self):
        testTask1 = "testTask1"
        testTask2 = "testTask2"
        testList = todolist.LinkedList()
        testList.insert_at_beginning("head")
        testList.insert_at_end(testTask1)
        testList.insert_at_end(testTask2)
        end = self.getEnd(testList.head)
        self.assertEqual(end.data, "testTask2")

    def test_insertAtPos_error(self):
        capturedOutput = io.StringIO()               # Create StringIO object
        sys.stdout = capturedOutput                   #  and redirect stdout.
        testList = todolist.LinkedList()
        testList.insert_at_pos(2, "test")
        self.assertTrue("Error:" in capturedOutput.getvalue())
        sys.stdout = sys.__stdout__

    
    def test_insertAtPos_0(self):
        testTask1 = "testTask1"
        testList = todolist.LinkedList()
        testList.insert_at_pos(0, testTask1)
        self.assertEqual(testList.head.data, testTask1)

    def test_insertAtPos(self):
        testTask1 = "testTask1"
        testTask2 = "testTask2"
        testTask3 = "testTask3"
        testTask4 = "testTask4"

        testList = todolist.LinkedList()
        testList.insert_at_beginning(testTask2)
        testList.insert_at_beginning(testTask1)
        testList.insert_at_end(testTask4)
        testList.insert_at_pos(2, testTask3)

        self.assertEqual(testList.head.next.next.data, testTask3)
    
    # def test_insertAfterTargetValue(self):
    #     # TODO
    #     return
    
    def test_pop_error(self):
        capturedOutput = io.StringIO()               # Create StringIO object
        sys.stdout = capturedOutput                   #  and redirect stdout.
        testList = todolist.LinkedList()
        testList.pop()
        self.assertTrue("Error:" in capturedOutput.getvalue())
        sys.stdout = sys.__stdout__
    
    def test_pop(self):
        testTask1 = "testTask1"
        testTask2 = "testTask2"
        testList = todolist.LinkedList()
        testList.insert_at_beginning(testTask2)
        testList.insert_at_beginning(testTask1)
        self.assertEqual(testList.size, 2)
        popped = testList.pop()
        self.assertEqual(popped.data, testTask1)
        self.assertEqual(testList.size, 1)
    
    def test_removeAt_error(self):
        capturedOutput = io.StringIO()               # Create StringIO object
        sys.stdout = capturedOutput     
        testList = todolist.LinkedList()
        testList.remove_at(1)
        self.assertTrue("Error:" in capturedOutput.getvalue())
        sys.stdout = sys.__stdout__
    
    def test_removeAt_0(self):
        testTask1 = "testTask1"
        testTask2 = "testTask2"
        testTask3 = "testTask3"
        testList = todolist.LinkedList()
        testList.insert_at_beginning(testTask3)
        testList.insert_at_beginning(testTask2)
        testList.insert_at_beginning(testTask1)
        removed = testList.remove_at(0)
        self.assertEqual(removed.data, testTask1)
    
    def test_removeAt_pos(self):
        testTask1 = "testTask1"
        testTask2 = "testTask2"
        testTask3 = "testTask3"
        testTask4 = "testTask4"
        testList = todolist.LinkedList()
        testList.insert_at_beginning(testTask4)
        testList.insert_at_beginning(testTask3)
        testList.insert_at_beginning(testTask2)
        testList.insert_at_beginning(testTask1)
        testList.remove_at(2)
        targetPos = testList.index_of(testTask4)
        self.assertEqual(targetPos, 2)
    
    def test_removeTargetValue_NoneError(self):
        capturedOutput = io.StringIO()               # Create StringIO object
        sys.stdout = capturedOutput     
        testList = todolist.LinkedList()
        testList.remove_target_value(None)
        self.assertTrue("Error:" in capturedOutput.getvalue())
        sys.stdout = sys.__stdout__
    
    def test_removeTargetValue(self):
        testTask1 = "testTask1"
        testTask2 = "testTask2"
        testTask3 = "testTask3"
        testList = todolist.LinkedList()
        testList.insert_at_beginning(testTask3)
        testList.insert_at_beginning(testTask2)
        testList.insert_at_beginning(testTask1)
        testList.remove_target_value(testTask1)
        self.assertEqual(testList.head.data, testTask2)

    def test_removeTarget_noValue(self):
        capturedOutput = io.StringIO()               # Create StringIO object
        sys.stdout = capturedOutput   
        testTask1 = "testTask1"
        testTask2 = "testTask2"
        testTask3 = "testTask3"
        testList = todolist.LinkedList()
        testList.insert_at_beginning(testTask3)
        testList.insert_at_beginning(testTask2)
        testList.insert_at_beginning(testTask1)
        testList.remove_target_value("testTask4")
        self.assertEqual(testList.head.data, testTask1)
        self.assertEqual(testList.size, 3)
        sys.stdout = sys.__stdout__

    def test_nodeAt(self):
        testTask1 = "testTask1"
        testTask2 = "testTask2"
        testTask3 = "testTask3"
        testTask4 = "testTask4"
        testList = todolist.LinkedList()
        testList.insert_at_beginning(testTask4)
        testList.insert_at_beginning(testTask3)
        testList.insert_at_beginning(testTask2)
        testList.insert_at_beginning(testTask1)
        target = testList.node_at(2)
        self.assertEqual(target.data, testTask3)

    def test_nodeAt_outOfRangeError(self):
        capturedOutput = io.StringIO()               # Create StringIO object
        sys.stdout = capturedOutput     
        testTask1 = "testTask1"
        testTask2 = "testTask2"
        testTask3 = "testTask3"
        testList = todolist.LinkedList()
        testList.insert_at_beginning(testTask3)
        testList.insert_at_beginning(testTask2)
        testList.insert_at_beginning(testTask1)
        target = testList.node_at(3)
        self.assertTrue("Error: Index not valid" in capturedOutput.getvalue())
        self.assertEqual(target, -1)
        sys.stdout = sys.__stdout__

