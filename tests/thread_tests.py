# -*- coding: utf-8 -*-
"""Unit test for Thread class."""
from collections import deque
from nose.tools import assert_equal, raises
from threadedmessenger.thread import Thread 
from threadedmessenger.message import Message 

@raises(TypeError)
def test_thread_id_type_error():
    """
    Test invalid input type for thread_id.
    """
    thread = Thread("1")

def test_thread():
    """
    Test if the Thread constructor initializes an object with correct member variables.
    """
    thread = Thread(1)
    assert_equal(thread.id, 1)
    assert_equal(thread.messages, deque([]))

@raises(TypeError)
def test_thread_add_type_error():
    """
    Test invalid input type for add method.
    """
    thread = Thread(1)
    thread.add(1)

def test_thread_add():
    """
    Test if a Thread object can add a message to its message queue.
    """
    thread = Thread(1)
    message_11 = Message(11, "Head of Message 1", "Content of Message 1")
    message_12 = Message(12, "Head of Message 2", "Content of Message 2")
    thread.add(message_11)
    assert_equal(thread.messages, deque([message_11]))
    thread.add(message_12)
    assert_equal(thread.messages, deque([message_12, message_11]))

def test_thread_str():
    """
    Test if the string representaion of a thread is correct
    """
    thread = Thread(1)
    message_11 = Message(11, "Head of Message 1", "Content of Message 11")
    message_12 = Message(12, "Head of Message 2", "Content of Message 12")
    thread.add(message_11)
    thread.add(message_12)
    assert_equal(str(thread), "1(12, 11)")
