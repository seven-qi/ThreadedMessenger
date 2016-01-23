# ThreadedMessenger
This is a threaded mailing list that will shows the most top k threads

## Installation
Go to the root directory of this package. Simply do:

    `python setup.py install`
  
## Getting Started
### Create new Message, Thread, and ThreadList
```python
from message import Message
from thread import Thread
from threadlist import ThreadList
message = Message(11, "This is the head of message 11", "This is the content of message 11")
thread = Thread(1)
threadlist = ThreadList(3) # k = 3
```

### Add message to threadlist
```python
threadlist.add(message, 1)
```

### Display top k threads
```python
threadlist.display()
```

## Test
In order to test the software, you need to have the following tools installed
    1. pip from http://pypi.python.org/pypi/pip
    2. distribute from http://pypi.python.org/pypi/distribute
    3. nose from http://pypi.python.org/pypi/nose/
    4. virtualenv from http://pypi.python.org/pypi/virtualen

After you got pip, you should be able to get the rest using:

    `pip install distribute`
    `pip install nose`
    `pip install virtualenv`

Then, simply do:
    
    `nosetests --with-coverage`

to run all the test cases and see the coverage.