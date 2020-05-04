#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Assignment 1

Create a simple class, MaxSizeList, that acts a little bit like a list, 
with a pre-configured limit on its size.  
'''

class MaxSizeList:
  def __init__(self, limit):
    self.max_size = limit
    self.innerlist = []

  def push(self, itm):
    self.innerlist.append(itm)
    if len(self.innerlist) > self.max_size:
        self.innerlist.pop(0)

  def get_list(self):
    return self.innerlist