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


"""
This is a function to test arithmetic brainfuck operations.
It produces a stack and positions the cursor at the top
Do not use loops in the footer, it messes with the expected outputed bytes.
"""
def run_arithmetic(file_content,stack=[],footer='>.>>.'):
    assert(footer.count('[') + footer.count(']') == 0)

    makestack = create_stack(stack)
    instruction = ''.join([makestack,file_content,footer])

    with BrainfuckMachine(instruction) as bfm:
        output = bfm.stdout.read(footer.count('.'))

    return int.from_bytes(output,'big')

