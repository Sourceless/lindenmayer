#!/usr/bin/env python

from callback import Callback

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
        self.use_memory = False
        self.program_counter = 0
        self.program = ''

    def relative_jump(self, jumpamount):
        self.program_counter += jumpamount - 1

    def relative_peek(self, peekamount):
        return self.program[self.program_counter + peekamount]

    def _use_memory(self):
        ''' _use_memory()
            pass interpreter as an argument to every callback in grammar
        '''
        for key, callback in self.grammar.iteritems():
            self.grammar[key] = Callback(callback, self)

    def load(self, key, value):
        ''' load(string key, Object value)
            load data into the interpreter's internal memory
        '''
        self.memory[key] = value

    def generate(self, program):
        ''' generate(string program) -> generator[callbacks]
            spits out one parsed callback at a time for use outside
        '''
        self.program = program

        if self.use_memory == True:
            self._use_memory()

        while self.program_counter < len(self.program):
            try:
                yield self.grammar[self.program[self.program_counter]]
            except KeyError, key:
                print 'skipping undefined char', key
            self.program_counter += 1

    def execute(self, program):
        ''' execute(string program)
            executes 'program' in the instance scope
        '''
        for fun in self.generate(program):
            fun()
