# -*- coding: utf-8 -*-
"""Unit test for ThreadList class."""
from collections import deque, OrderedDict
from StringIO import StringIO
from nose.tools import assert_equal, raises
from threadedmessenger.message import Message 
from threadedmessenger.threadlist import ThreadList

@raises(TypeError)
def test_threadlist_k_type_error():
    """
    Test invalid input type for k.
    """
    threadlist = ThreadList("1")

def test_threadlist():
    """
    Test if the ThreadList constructor initializes an object with correct member variables.
    """
    threadlist = ThreadList(3)

    assert_equal(threadlist.threads, OrderedDict())
    assert_equal(threadlist.display_size, 3)

@raises(TypeError)
def test_threadlist_add_message_type_error():
    """
    Test invalid input type for add method, message argument.
    """
    threadlist = ThreadList(3)
    threadlist.add(1, 1)

@raises(TypeError)
def test_threadlist_add_thread_id_type_error():
    """
    Test invalid input type for add method, thread_id argument.
    """
    threadlist = ThreadList(3)
    message = Message(1, "Head of Message 1", "Content of Message 1")
    threadlist.add(message, "1")

def test_threadlist_add():
    """
    Test if a ThreaList object can add a message to the correct thread and move the
        thread to the top of the list.
    """
    def compare_threads(messages, thread_ids, threadlist):
        """
        Check the state of the threadlist.
        """
        for index, (thread_id, thread) in enumerate(threadlist.threads.items()):
            assert_equal(thread_id, thread_ids[index])
            assert_equal(thread.messages, messages[index])

    threadlist = ThreadList(1)

    # Add M11, T1
    message_11 = Message(11, "Head of Message 11", "Content of Message 11")
    threadlist.add(message_11, 1)
    messages = [deque([message_11])]
    thread_ids = [1]
    compare_threads(messages, thread_ids, threadlist)

    # Add M21, T2
    message_21 = Message(21, "Head of Message 21", "Content of Message 21")
    threadlist.add(message_21, 2)
    messages = [deque([message_11]), deque([message_21])]
    thread_ids = [1, 2]
    compare_threads(messages, thread_ids, threadlist)

    # Add M12, T1
    message_12 = Message(12, "Head of Message 22", "Content of Message 22")
    threadlist.add(message_12, 1)
    messages = [deque([message_21]), deque([message_12, message_11])]
    thread_ids = [2, 1]
    compare_threads(messages, thread_ids, threadlist)

@raises(TypeError)
def test_threadlist_display_out_type_error():
    """
    Test invalid input type for display method, out argument.
    """
    threadlist = ThreadList(3)
    threadlist.display(1)

def test_threadlist_display():
    """
    Test ThreadList class str method.
    """
    # Create a new thread list that shows only the top 3 threads.
    threadlist = ThreadList(3)

    # Add (M7, T13). State: [7(13)]
    message_13 = Message(13, "Head of Message 13", "Content of Message 13")
    threadlist.add(message_13, 7)
    out = StringIO()
    threadlist.display(out)
    assert_equal(out.getvalue().strip(), "[7(13)]")

    # Add (M5, T99). State: [99(5), 7(13)]
    message_5 = Message(5, "Head of Message 5", "Content of Message 5")
    threadlist.add(message_5, 99)
    out = StringIO()
    threadlist.display(out)
    assert_equal(out.getvalue().strip(), "[99(5), 7(13)]")

    # Add (M4, T11). State: [11(4), 99(5), 7(13)]
    message_4 = Message(4, "Head of Message 4", "Content of Message 4")
    threadlist.add(message_4, 11)
    out = StringIO()
    threadlist.display(out)
    assert_equal(out.getvalue().strip(), "[11(4), 99(5), 7(13)]")

    # Add (M44, T99). State: [99(44, 5), 11(4), 7(13)]
    message_44 = Message(44, "Head of Message 44", "Content of Message 44")
    threadlist.add(message_44, 99)
    out = StringIO()
    threadlist.display(out)
    assert_equal(out.getvalue().strip(), "[99(44, 5), 11(4), 7(13)]")

    # Add (M1, T11). State: [1(1), 99(44, 55), 11(4), 7(13)] => [[1(1), 99(44, 55), 11(4)]
    message_1 = Message(1, "Head of Message 1", "Content of Message 1")
    threadlist.add(message_1, 1)
    out = StringIO()
    threadlist.display(out)
    assert_equal(out.getvalue().strip(), "[1(1), 99(44, 5), 11(4)]")

    # Add (M2, T7). State: [7(2, 13), 1(1), 99(44, 55), 11(4)] => [7(2, 13), 1(1), 99(44, 55)]
    message_2 = Message(2, "Head of Message 2", "Content of Message 2")
    threadlist.add(message_2, 7)
    out = StringIO()
    threadlist.display(out)
    assert_equal(out.getvalue().strip(), "[7(2, 13), 1(1), 99(44, 5)]")

