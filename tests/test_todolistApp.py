import sys
sys.path.append('../src')

import unittest
from unittest.mock import patch
import io
import todolistApp

class TestTodolistApp(unittest.TestCase):

    @patch('builtins.input', side_effect=["QUIT"])
    def test_startAndEnd(self, mock_inputs):
        capturedOutput = io.StringIO()               # Create StringIO object
        sys.stdout = capturedOutput
        app = todolistApp.TodolistApp()
        app.start()
        self.assertTrue("Welcome" in capturedOutput.getvalue())
        self.assertTrue("App Ended." in capturedOutput.getvalue())
        sys.stdout = sys.__stdout__

    @patch('builtins.input', side_effect=["ABC", "QUIT"])
    def test_invalidInput(self, mock_inputs):
        capturedOutput = io.StringIO()               # Create StringIO object
        sys.stdout = capturedOutput
        app = todolistApp.TodolistApp()
        app.start()
        self.assertTrue(
            "Error: Command is not valid." in capturedOutput.getvalue())
        sys.stdout = sys.__stdout__

    @patch('builtins.input', side_effect=["IB,task1", "QUIT"])
    def test_insertBeginning(self, mock_inputs):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        app = todolistApp.TodolistApp()
        app.start()
        self.assertTrue("is inserted" in capturedOutput.getvalue())
        sys.stdout = sys.__stdout__

    @patch('builtins.input', side_effect=["IB,task1", "POP", "QUIT"])
    def test_insertAndPop(self, mock_inputs):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        app = todolistApp.TodolistApp()
        app.start()
        self.assertTrue(
            "Task  task1  is finished" in capturedOutput.getvalue())
        sys.stdout = sys.__stdout__

    @patch('builtins.input', side_effect=["IB,task1", "IE,task2", "SEARCH,task1", "QUIT"])
    def test_insertAndSearch(self, mock_inputs):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        app = todolistApp.TodolistApp()
        app.start()
        self.assertTrue(
            "Task  task1  is found at index  0" in capturedOutput.getvalue())
        sys.stdout = sys.__stdout__

    @patch('builtins.input', side_effect=["IB,task2", "IE,task3", "IP,0,task1", "QUIT"])
    def test_insertAtPosition(self, mock_inputs):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        app = todolistApp.TodolistApp()
        app.start()
        self.assertTrue(
            "Task  task1  is inserted at index  0" in capturedOutput.getvalue())
        sys.stdout = sys.__stdout__

    @patch('builtins.input', side_effect=["IB,task1", "IE,task2", "FIND,0", "QUIT"])
    def test_insertAndFind(self, mock_inputs):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        app = todolistApp.TodolistApp()
        app.start()
        self.assertTrue(
            "Task  task1  is found at index  0" in capturedOutput.getvalue())
        sys.stdout = sys.__stdout__

    @patch('builtins.input', side_effect=["IB,task2", "IB,task1", "RA,0", "QUIT"])
    def test_removeAt(self, mock_inputs):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        app = todolistApp.TodolistApp()
        app.start()
        self.assertTrue(
            "Task  task1  located at index  0  is removed" in capturedOutput.getvalue())
        sys.stdout = sys.__stdout__

    @patch('builtins.input', side_effect=["IB,task2", "IB,task1", "IS,task1,taskX", "QUIT"])
    def test_removeAt(self, mock_inputs):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        app = todolistApp.TodolistApp()
        app.start()
        self.assertTrue(
            "Task  taskX  is inserted after task  task1" in capturedOutput.getvalue())
        sys.stdout = sys.__stdout__

    @patch('builtins.input', side_effect=["IB,task2", "IB,task1", "RT,task1", "QUIT"])
    def test_removeTarget(self, mock_inputs):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        app = todolistApp.TodolistApp()
        app.start()
        self.assertTrue(
            "Task  task1  is removed" in capturedOutput.getvalue())
        sys.stdout = sys.__stdout__
