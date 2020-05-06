#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import pickle


class ConfigKeyError(Exception):

    def __init__(self, this, key):
        
        self.key = key
        self.keys = this.keys()

    def __str__(self):
        
        return f"key '{self.key}' not found. Available keys: {', '.join(self.keys)}"

class ConfigPickleDict(dict):

    config_dir = './configs'

    def __init__(self, picklename):

        self._filename = os.path.join(ConfigPickleDict.config_dir, picklename + '.pickle')
        if not os.path.isfile(self._filename):
            try:
                with open(self._filename, 'w') as fh:
                    pickle.dump({}, fh)
            except IOError:
                raise IOError('arg to ConfigDict must be valid path name')
        with open(self._filename) as fh:
            pkl = pickle.load(fh)
            self.update(pkl)

    def __getitem__(self, key):

        if not key in self:
            raise ConfigKeyError(self, key)
        
        return dict.__getitem__(self, key)

    def __setitem__(self, key, value):

        dict.__setitem__(self, key, value)
        with open(self._filename, 'w') as fh:
            pickle.dump(self, fh)