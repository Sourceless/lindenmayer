#!/usr/bin/env python
# Author: Laurence Joseph Smith [ljs/Sourceless]
# GitHub: http://www.github.com/Sourceless

import sys
from interpreter import Interpreter

## Internal Function definitions
def _inc_pointer(interp):
    _check_tape_ptr(interp)
    interp.memory['ptr'] += 1

def _dec_pointer(interp):
    _check_tape_ptr(interp)
    interp.memory['ptr'] -= 1

def _check_tape_ptr(interp):
    if interp.memory['ptr'] < 0:
        interp.memory['tape'] = ([0]*-interp.memory['ptr']) + interp.memory['tape']
        interp.memory['ptr'] = 0
    if interp.memory['ptr'] >= len(interp.memory['tape']):
        interp.memory['tape'] = interp.memory['tape'] + [0]*(interp.memory['ptr']+len(interp.memory['tape'])-1)

def _set_tape_pos(interp, amount):
    _check_tape_ptr(interp)
    interp.memory['tape'][interp.memory['ptr']] += amount

def _inc_data(interp):
    _set_tape_pos(interp, 1)

def _dec_data(interp):
    _set_tape_pos(interp, -1)

def _output(interp):
    _check_tape_ptr(interp)
    sys.stdout.write('%s' % chr(interp.memory['tape'][interp.memory['ptr']]))
    sys.stdout.flush()

##def _debug_output(interp):
##    _check_tape_ptr(interp)
##    print "D:", interp.memory['tape'][interp.memory['ptr']]

def _input(interp):
    myinput = ''
    
    while len(myinput) != 1:
        myinput = raw_input('> ')
        if len(myinput) != 1:
            print 'Single char inputs only'

    _set_tape_pos(interp, ord(myinput))

def _if_zero_jump_forward(interp):
    if interp.memory['tape'][interp.memory['ptr']] == 0:
       loop = 1
       count = 1
       while loop:
           if interp.relative_peek(count) == '[':
               loop += 1
           elif interp.relative_peek(count) == ']':
               loop -= 1
           count += 1

       interp.relative_jump(count+1)

def _if_nonzero_jump_back(interp):
    if interp.memory['tape'][interp.memory['ptr']] != 0:
        loop = 1
        count = -1
        while loop:
            if interp.relative_peek(count) == ']':
                loop += 1
            elif interp.relative_peek(count) == '[':
                loop -= 1
            count -= 1

        interp.relative_jump(count+1)


## Main example routine
def main():
    grammar = { '>':_inc_pointer,
                '<':_dec_pointer,
                '+':_inc_data,
                '-':_dec_data,
                '.':_output,
                ',':_input,
                '[':_if_zero_jump_forward,
                ']':_if_nonzero_jump_back
              }
    data =  '++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>.' # 'Hello world'

    i = Interpreter(grammar)
    i.use_memory = True
    i.load('tape',[0])
    i.load('ptr',0)
    i.load('loop',0)
    i.execute(data)

if __name__ == '__main__':
    main()
