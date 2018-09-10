# -*- coding: UTF-8 -*-
from __future__ import print_function


class Node(object):
    def __init__(self, data, next_data=None):
        self.data = data
        self.next = next_data


class Stack(object):
    def __init__(self, top=None):
        self.top = top

    def push(self, data):
        self.top = Node(data, self.top)

    def pop(self):
        if self.top is None:
            return None
        data = self.top.data
        self.top = self.top.next
        return data

    def peek(self):
        return self.top.data if self.top is not None else None

    def is_empty(self):
        return self.top is None
