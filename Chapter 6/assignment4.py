#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os


class ConfigKeyError(Exception):

    def __init__(self, this, key):
        
        self.key = key
        self.keys = this.keys()

    def __str__(self):
        
        return f"key '{self.key}' not found. Available keys: {', '.join(self.keys)}"

class ConfigDict(dict):

    def __init__(self, filename):

        self._filename = filename
        if not os.path.isfile(self._filename):
            try:
                open(self._filename, 'w').close()
            except IOError:
                raise IOError('arg to ConfigDict must be valid path name')
        with open(self._filename) as fh:
            for line in fh:
                line = line.rstrip()
                key, value = line.split('=', 1)
                dict.__setitem__(self, key, value)

    def __getitem__(self, key):

        if not key in self:
            raise ConfigKeyError(self, key)
        
        return dict.__getitem__(self, key)

    def __setitem__(self, key, value):

        dict.__setitem__(self, key, value)
        with open(self._filename, 'w') as fh:
            for key, value in self.items():
                fh.write(f"{key}={value}")