# -*- coding: utf-8 -*-
"""This modules deals with the message in the email thread"""
import logging

class Message(object):
    """
    A message with head and content.
    """
    def __init__(self, message_id, head, content):
        """
        Initialize a Message with id, head and content.
        
        Args:
            message_id (int): The unique id of this message.
            head (str): The head of this message.
            content (str): The content of this message.
        
        Raises:
            TypeError: If any input arg is not in correct type, TypeError will be raised.
        """
        logging.info("Trying to create message with id = %s ...", str(message_id))
        if not isinstance(message_id, int):
            raise TypeError("message_id should be int type, got " + str(type(message_id)))
        if not isinstance(head, str):
            raise TypeError("head should be str type, got " + str(type(head)))
        if not isinstance(content, str):
            raise TypeError("content should be str type, got " + str(type(content)))
        self._id = message_id 
        self._head = head 
        self._content = content
        logging.info("Creates message_%s", str(message_id))

    @property
    def id(self):
        return self._id

    @property
    def head(self):
        return self._head
    
    @property
    def content(self):
        return self._content

    def __str__(self):
        """
        Use the id str as the string representation of the message object.
        
        Returns:
            str: The string representation of this message object.
        """
        return str(self._id)
