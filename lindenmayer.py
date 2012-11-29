#!/usr/bin/env python

import generator, interpreter

class Lindenmayer:
    ''' Lindenmayer(dict rules, dict callbacks):
        A class for implementing L-Systems.

        rules is a dict in format 
            {'c': 'abc'}
        where 'c' can be any char, and 'abc' is the evolution that char undergoes

        callbacks is a dict in format
            {'c': callback_for_c }
        where 'c', again, can be any char, and call_back_for_c, is, well, a callback
        You can use the callback.Callback object if you need to pass in arguments 
        with a function callback.
    '''

    def __init__(self, rules, callbacks):
        self.rules      = rules
        self.callbacks  = callbacks
        self.generator  = generator.Generator
        self.interpreter= interpreter.Interpreter(callbacks)

    def run(self, instructions, generations=0):
        ''' run(string instructions, int generations)
            evolves _instructions_ through _generations_ and returns a generator
        '''

        self.generator = self.generator(instructions, self.rules)

        for _ in xrange(generations):
            instructions = self.generator.next()

        return self.intepreter.generate(instructions)
