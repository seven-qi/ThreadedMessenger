# -*- coding: utf-8 -*-
"""This module deals with the email threadlist."""

import sys
from collections import OrderedDict
from StringIO import StringIO
from threadedmessenger.message import Message
from threadedmessenger.thread import Thread
import logging

class ThreadList(object):
    """
    A threadlist with a list of threads and only shows the most recent k threads.
    """
    def __init__(self, k):
        """
        Initialize a ThreaList with k as number of threads to be displayed.
        
        Args:
            k (int): The number of the most recent threads to be displayed.
        
        Raises:
            TypeError: If any input arg is not in correct type, TypeError will be raised.
        """
        logging.info("Trying to create threadlist ...")
        if not isinstance(k, int):
            raise TypeError("k should be int type, got " + str(type(k)))
        self._display_size = k 
        self._threads = OrderedDict()
        logging.info("Creates threadlist.")

    @property
    def display_size(self):
        return self._display_size
    
    @display_size.setter
    def display_size(k):
        self._display_size = k

    @property
    def threads(self):
        return self._threads
    

    def add(self, message, thread_id):
        """
        Adds a message to a thread, and put the thread to the front of the queue.
        
        Args:
            message (str): The new message to be added to a thread.
            thread_id (int): The is of the thread that should contain the new message.
        
        Raises:
            TypeError: If any input arg is not in correct type, TypeError will be raised.
        """
        logging.info("Trying to add message_%s to threadlist ...", str(message) if message else "")
        if not isinstance(thread_id, int):
            raise TypeError("thread_id should be int type, got " + str(type(thread_id)))
        if not isinstance(message, Message):
            raise TypeError("message should be Message type, got " + str(type(message)))
        if thread_id in self._threads:
            thread = self._threads.pop(thread_id)
            thread.add(message)
        else:
            thread = Thread(thread_id)
            thread.add(message)
        self._threads[thread_id] = thread
        logging.info("Added message_%s to threalist.", str(message) if message else "")


    def display(self, out=sys.stdout):
        """
        Wirte out the top k threads to the output stream
        
        Args:
            out (file/StringIO, optional): The default output stream is the standard output, 
            but it can also be StringIO for testing.
        
        Raises:
            TypeError: If any input arg is not in correct type, TypeError will be raised.
        """
        logging.info("Trying to display top %s threads ...", str(self._display_size))
        if not isinstance(out, file) and not isinstance(out, StringIO):
            raise TypeError("out should be file type or StringIO, got " + str(type(out)))
        out.write('[' + ', '.join([str(t[1]) for t in self._threads.items()[::-1][:self._display_size]]) + ']\n')
        logging.info("Displays top %s threads.", str(self._display_size))
