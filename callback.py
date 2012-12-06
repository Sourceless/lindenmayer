#!/usr/bin/env python

class Callback:
    ''' Callback(function fun, tuple args)
        Utility class for creating a simple callback for deferred calling.
        Be careful about side effects and things.
    '''
    def __init__(self, fun, *args):
        self.fun = fun
        self.args = args

    def __call__(self):
        ''' __call__()
            call the deffered function
        '''
        try:
            return self.fun(*self.args)
        except ValueError:
            return self.fun(self.args)
