#!/usr/bin/env python
# Author: Laurence Joseph Smith [ljs/Sourceless]
# GitHub: http://www.github.com/Sourceless

import turtle
from generator import Generator
from interpreter import Interpreter

## Function Defs
def _push_state(interp):
    ''' _push_state(Interpreter interp)
        save turtle state in interp memory
    '''
    t = interp.memory["turtle"]
    interp.memory["state"].append((t.pos(), t.heading()))

def _pop_state(interp):
    ''' _pop_state(Interpreter interp)
        restore turtle state from interp memory
    '''
    mypos, myheading = interp.memory["state"].pop()
    interp.memory["turtle"].setpos(mypos)
    interp.memory["turtle"].setheading(myheading)

def _forwards(interp):
    ''' _forwards(Interpreter interp)
        move the turtle forward
    '''
    t = interp.memory["turtle"]
    t.down()
    t.forward(50)
    t.up()

def _left(interp):
    t = interp.memory["turtle"]
    t.left(35)

def _right(interp):
    t = interp.memory["turtle"]
    t.right(35)


## Example Routine
def main():
    # Inputs for interpreter and generator
    grammar = {'[':_push_state, ']':_pop_state,
               'F':_forwards, 'L':_left, 'R':_right,
              }
    rules   = {'T':'F[LT][RT]'}
    data = 'T'
    generations = 5

    # Create a generator
    g = Generator(data, rules)
    data = g.nth_generation(generations)

    # Create and set up interpreter
    i = Interpreter(grammar)
    i.use_memory = True # Use the interpreter's memory, 
                        #  i.e. pass the interpreter as the 
                        # first argument to every callback in the grammar

    # Initialise a turtle
    t = turtle.Turtle()
    t.hideturtle()
    t.left(90)

    # Load required items into interpreter memory
    i.load('turtle', t) # Load in a turtle
    i.load('state', []) # Load in an empty list for turtle's state stack

    i.execute(data)
    
    turtle.exitonclick()

if __name__=='__main__':
    main()
