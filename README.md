# CISC593_VnV_fina

## app structure
The app is structured with two layers.
1. todolist.py: core functionalities to handle underlying data structure and provide operations interface like insert, remove. 
2. todolistApp.py: provides command interface with print out messages. 

### to run 
```
python ./src/todolistApp.py
```

## unit tests

### run unit tests
1. install coverage.py

```batch
   pip install coverage
```

2. run tests
```batch
coverage run --source=../src -m unittest
coverage report -m
```

### unit test utilities
Uses python built-in unit test framework to build tests. 
For the interface layer, unittest.mock is used to mock user inputs. 

### unit test cases
* todolist.py
  1. Node
     1. test node with data and next properties
  2. LinkedList
     1. test linked list with head and size properties
  3. printList
     1. test linked list can be printed with index and value
  4. LinkedList - insert at the beginning
     1. test inserting a task at the beginning
  5. LinkedList - insert at the end
     1. insert at the end when list is empty
     2. insert at the end when list is not empty
  6. LinkedList - insert at position
     1. exception : position out of range
     2. insert at position 0 
     3. insert in the middle position
  7. LinkedList - pop
     1. exception : pop an empty list
     2. pop a non-empty list
  8. LinkedList - removeAt
     1. exception: remove out of range
     2. remove at position 0
     3. remove at position 2
  9. LinkedList - removeTargetValue
     1.  remove head with value
     2.  exception: remove non-exist value
  10. LinkedList - nodeAt
      1.  test node at position 2
      2.  exception: remove out of range
  
* todolistApp.py
  1. test greet and end message
  2. Exception: test invalid command input
  3. test command: IB
  4. test command: POP
  5. test command: IE, SEARCH
  6. test command: IP
  7. test command: FIND
  8. test command: RA
  9. test command: IS
  10. test command: RT
  

### result

Hit overall 93% code coverage. Generally, 70% to 80% code coverage is considered a high standard for applications. 

Name              Stmts   Miss  Cover   Missing

---------------------------------------------------------------------------------------
todolist.py        124      7    94%   67-68, 75, 77-78, 144-145
todolistApp.py      87      7    92%   75-79, 112-113
---------------------------------------------------------------------------------------
TOTAL              211     14    93%