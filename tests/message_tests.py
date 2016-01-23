# -*- coding: utf-8 -*-
'''
Created on 2016-01-21 19:43
@summary: 
@author: sevensevens
'''
from nose.tools import assert_equal, raises
from threadedmessenger.message import Message 

@raises(TypeError)
def test_message_id_type_error():
    """
    Test invalid input type for message_id.
    """
    message = Message("1", "Head of Message 1", "Content of Message 1")

@raises(TypeError)
def test_message_head_type_error():
    """
    Test invalid input type for head.
    """
    message = Message(1, 1, "Content of Message 1")

@raises(TypeError)
def test_message_content_type_error():
    """
    Test invalid input type for content.
    """
    message = Message(1, "Head of Message 1", 1)

def test_message():
    """
    Test Message class.
    """
    message = Message(1, "Head of Message 1", "Content of Message 1")
    assert_equal(message.id, 1)
    assert_equal(message.head, "Head of Message 1")
    assert_equal(message.content, "Content of Message 1")

def test_message_str():
    """
    Test Message class.
    """
    message = Message(1, "Head of Message 1", "Content of Message 1")
    assert_equal(str(message), "1")
