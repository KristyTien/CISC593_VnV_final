import unittest
import todolistApp
import sys
import io
import mock
from unittest.mock import patch


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

    @patch('builtins.input', side_effect=["IB,task1", "QUIT"])
    def test_insertBeginning(self, mock_inputs):
        capturedOutput = io.StringIO()               # Create StringIO object
        sys.stdout = capturedOutput         
        app = todolistApp.TodolistApp()
        app.start()
        self.assertTrue("is inserted" in capturedOutput.getvalue())
        sys.stdout = sys.__stdout__
    
    @patch('builtins.input', side_effect=["IB,task1", "POP", "QUIT"])
    def test_insertAndPop(self, mock_inputs):
        capturedOutput = io.StringIO()               # Create StringIO object
        sys.stdout = capturedOutput         
        app = todolistApp.TodolistApp()
        app.start()
        self.assertTrue("Task  task1  is finished" in capturedOutput.getvalue())
        sys.stdout = sys.__stdout__



    
