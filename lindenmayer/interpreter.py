#!/usr/bin/env python

class Interpreter:
    ''' Interpreter(grammar={})
        Basic one-char-at-a-time interpreter for l-systems and similar.
        Main argument is grammar, a dictionary with single-character keys
        mapping to callbacks.

        There is also a .memory attribute available for storing data inside
        the interpreter - keeping it self contained.

        generate() will yield a function at a time for use in a different scope
        execute()  will execute the callbacks within the interpreter
    '''
    def __init__(self, grammar={}):
        self.grammar = grammar
        self.memory = {}

    def generate(self, program):
        ''' generate(string program) -> generator[callbacks]
            spits out one parsed callback at a time for use outside
        '''
        for char in program:
            yield self.grammar[char]

    def execute(self, program):
        ''' execute(string program)
            executes 'program' in the instance scope
        '''
        for fun in self.generate(program):
            fun()
