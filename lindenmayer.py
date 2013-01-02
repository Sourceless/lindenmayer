#!/usr/bin/env python

import generator
import interpreter

class LSystemMachine:
    ''' class LSystemMachine(string data, dict rules, dict grammar,
                             bool use_memory=False, memory={})
        An implementation of a machine to intepret l-system grammars
    '''

    def __init__(self, data, rules, grammar, use_memory=False, memory={}):
        self.generator   = generator.Generator(data, rules)
        self.interpreter = interpreter.Interpreter(grammar)
        
        if use_memory:
            self.interpreter.use_memory()
            for k, v in memory.iteritems():
                self.interpreter.

    def iter_nth(self, n):
        ''' run_nth(int n)
            Calculate the nth generation of L-System and yield functions
            for execution elsewhere.
        '''

        program = self.generator.nth_generation(n)
        
        for fun in self.interpreter.generate(program)
            yield fun

    def execute_nth(self, n):
        ''' execute_nth(int n)
            Calculate nth generation of L-System and execute.
        '''
        for fun in self.iter_nth(n):
            fun()
