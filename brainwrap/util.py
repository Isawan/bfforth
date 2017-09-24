#!/usr/bin/env python3
from brainwrap.machine import BrainfuckMachine
TAPESIZE=30000

"""
This function generates a header to initilise the stack
and position cursor at the top cell
"""
def create_stack(stack):
    prehead = map(lambda x: ''.join([
        ''.join(['+']*(x//2**8)),
        '>+>',
        ''.join(['+']*(x%2**8))]), 
        stack)
    head = ''.join(['+>',
            '>+>'.join(prehead),
            '<<<'])
    return head

def init_state(tape, start_index):
    mem = '>'.join(map(lambda x : ''.join(['+']*x),tape))
    # Now put cursor in correct position
    position = ''.join(['<']*mem.count('>')+['>']*start_index)
    return mem+position


"""
This is a function to test arithmetic brainfuck operations.
It produces a stack and positions the cursor at the top
Returns integer at the top of the stack.
Do not use loops in the footer, it messes with the expected outputed bytes.
"""
def run_arithmetic(file_content,stack=[],footer='>.>>.'):
    assert(footer.count('[') + footer.count(']') == 0)

    makestack = create_stack(stack)
    instruction = '\n'.join([makestack,file_content,footer])

    with BrainfuckMachine(instruction) as bfm:
        output = bfm.stdout.read(footer.count('.'))

    return int.from_bytes(output,'big')

"""
This is a function to test dataspace operations.
Returns a data stream of outputs
"""
def run_dataspace(file_content,tape=[0],init_cursor=0,footer='.'):
    assert(init_cursor >= 0)
    maketape = init_state(tape,init_cursor)
    instruction = '\n'.join([maketape,file_content,footer])
    with BrainfuckMachine(instruction,tapesize=700000) as bfm:
        return bfm.stdout.read()
