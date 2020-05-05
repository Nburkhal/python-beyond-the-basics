#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Assignment 2

Create a very simple inheritance hierarchy of three classes that write to text files.  

LogFile(WriteFile):  its instance writes a date and message to a log file:  

2015-01-21 18:35   this is a log message


DelimFile (WriteFile):  its instance writes values separated by a delimeter:   

a,b,c,d


WriteFile(object):  the parent class to both LogFile and DelimFile, 
does work that is common between them.   Not intended to be instantiated.  
'''

import os
import abc
import datetime as dt


class WriteFile:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def write(self):
        '''writes item to file'''
        return

    def __init__(self, filename):
        self.filename = filename

    def write_lines(self, txt):
        with open(self.filename, 'a') as f:
            f.write(txt + '\n')

class LogFile(WriteFile):
    def write(self, line):
        dt_str = dt.datetime.now().strftime('%Y-%m-%d %H:%M')
        self.write_lines(f'{dt_str}---------------{line}')

class DelimFile(WriteFile):
    def __init__(self, filename, delimiter):
        super(DelimFile, self).__init__(filename)
        self.delimiter = delimiter

    def write(self, mylist):
        line = self.delimiter.join(mylist)
        self.write_lines(line)