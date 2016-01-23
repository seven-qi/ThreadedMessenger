Getting Started
===============

Create new Message, Thread, and ThreadList
------------------------------------------

.. code-block:: python

   from message import Message
   from thread import Thread
   from threadlist import ThreadList
   # a meesage with id 11
   message_11 = Message(11, "This is the head of message 11", "This is the content of message 11") 
   thread_1 = Thread(1) # a thread with id 1, queue of messages is empty
   threadlist = ThreadList(2) # k = 2, a threadlist showing the most recent 3 threads

Add message to threadlist
-------------------------

.. code-block:: python

   threadlist.add(message_11, 1) # add message_11 to thread_1, threadlist state: [1(11)]

Display most k recent threads
-----------------------------

.. code-block:: python

   # a meesage with id 12
   message_12 = Message(12, "This is the head of message 12", "This is the content of message 12") 
   # a meesage with id 21
   message_21 = Message(21, "This is the head of message 21", "This is the content of message 21") 
   # a meesage with id 31
   message_31 = Message(31, "This is the head of message 31", "This is the content of message 31")
   thread_2 = Thread(2) # a thread with id 2, queue of messages is empty
   thread_3 = Thread(3) # a thread with id 3, queue of messages is empty

   threadlist.add(message_21, 2) # threadlist state: [2(21), 1(11)]
   threadlsit.display() # print out [2(21), 1(11)]

   threadlist.add(message_31, 3) # threadlist state: [3(31), 2(21), 1(11)] => [3(31), 2(21)]
   threadlist.display() # print out [3(31), 2(21)]

   threadlist.add(message_12, 1) # threadlist state: [1(12, 11), 3(31), 2(21)] => [1(12, 11), 3(31)]
   threadlist.display() # print out [1(12, 11), 3(31)]


