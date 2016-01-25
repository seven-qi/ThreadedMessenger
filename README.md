# ThreadedMessenger
This is a threaded mailing list that will shows the most top k threads

## Design and Ideas
### Data Structure and Implementation
For the threaded messenger, what we need to do is to be able to store the messages in a thread,
and store threads in a threadlist, all of them should be in the order of insertion time with most recent ones at the top.
#### Messenger Class
Stores the m_id, m_head, and m_content
#### Thread Class
Uses a queue to stor the messages with the most recent ones at the front.
#### ThreadList Class
Inorder to keep track of the insertion order and be able to search the Thread object by its id, we need to use OrderedDict,
whose underlying implementation is a doubly linkedlist with each node as the value as a hash_map. 

### OO Design
Singleton vs Factory
I have thought about creating ThreadList as a Singleton given that one app can only has ThreadList. 
However, I think we could reuse the implementation for the ThreadList to get 
MailThreadList, WhatsAppThreadList, MessengerThreadList, etc. So I didn't use singleton.

## Samples
To run some example, go to the root folder of the package and do:
```python
python main.py
```
It should show:
```
Create a new thread list that shows only the top 3 threads.
State: 
[]

State: 
[7(13)]

Add (M5, T99)
State: 
[99(5), 7(13)]

Add (M4, T11)
State: 
[11(4), 99(5), 7(13)]

Add (M44, T99)
State: 
[99(44, 5), 11(4), 7(13)]

Add (M1, T11)
State: 
[1(1), 99(44, 5), 11(4)]

Add (M2, T7)
State: 
[7(2, 13), 1(1), 99(44, 5)]

```

## Logging
I use spdlog (https://github.com/gabime/spdlog) to do the logging, but it turns out it's not quite compatible with the VS test framework so I disabled it by default.

## Documentation
Please go to <root_of_source>/docs/_build/html/ and open the index.html file. You should see a detailed documentation page.


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
Something like:
```
$ nosetests --with-coverage
.................
Name                              Stmts   Miss  Cover   Missing
---------------------------------------------------------------
threadedmessenger.py                  0      0   100%   
threadedmessenger/message.py         20      0   100%   
threadedmessenger/thread.py          22      0   100%   
threadedmessenger/threadlist.py      31      0   100%   
---------------------------------------------------------------
TOTAL                                73      0   100%   
----------------------------------------------------------------------
Ran 17 tests in 0.014s

OK

```



