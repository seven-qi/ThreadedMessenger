# -*- coding: utf-8 -*-
"""This module deals with the email thread in the thread list"""

from collections import deque
from threadedmessenger.message import Message

class Thread(object):
    """
    A thread with a queue of messages.
    """
    def __init__(self, thread_id):
        """
        Initialize a Thread with id.

        Args:
            thread_id (int): The unique id of this thread.
        
        Raises:
            TypeError: If any input arg is not in correct type, TypeError will be raised.
        """
        if not isinstance(thread_id, int):
            raise TypeError("thread_id should be int type, got " + str(type(thread_id)))
        self._id = thread_id 
        self._messages = deque()

    @property
    def id(self):
        return self._id

    @property
    def messages(self):
        return self._messages
    

    def __str__(self):
        
        """
        Use the id str as the string representation of the thread object.
        
        Returns:
            str: The string representation of this thread object.
        """
        ret = str(self._id) + '('
        ret += ', '.join([str(m) for m in self._messages])
        ret += ')'
        return ret

    def add(self, message):
        """
        Add a message to the message queue of this thread
        
        Args:
            message (Message): The message to be added to the message queue of this thread
        
        Raises:
            TypeError: If any input arg is not in correct type, TypeError will be raised.
        """
        if not isinstance(message, Message):
            raise TypeError("message should be Message type, got " + str(type(message)))
        self._messages.appendleft(message)
