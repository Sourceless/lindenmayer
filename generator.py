#!/usr/bin/env python

class Generator:
    ''' Generator(data, rules)
        A generator class for L-systems.
    '''
    def __init__(self, data, rules):
        self.data = data
        self.rules = rules

    def _next_generation(self):
        ''' _next_generation()
            Computes and stores the next generation.
        '''
        gen = list(self.data)

        for i in xrange(len(gen)):
            if gen[i] in self.rules.keys():
                gen[i] = self.rules[gen[i]]

        self.data = ''.join(gen)

    def next(self):
        self._next_generation()
        return self.data

    def nth_generation(self, n):
        for _ in xrange(n):
            self._next_generation()
        return self.data
