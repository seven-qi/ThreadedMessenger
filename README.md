# ThreadedMessenger
This is a threaded mailing list that will shows the most top k threads

## Installation
Go to the root directory of this package. Simply do:

  `python setup.py install`
  
## Getting Started
### Create new Message, Thread, ThreadList
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
