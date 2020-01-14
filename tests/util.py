#!/usr/bin/env python3
import tempfile
import subprocess

TAPESIZE=30000

def create_header(stack):
    """
    This function generates a header to initilise the stack
    """
    prehead = map(lambda x: ''.join([
        ''.join(['+']*(x//2**8)),
        '>+>',
        ''.join(['+']*(x%2**8))]), 
        stack)
    head = ''.join(['+>',
            '>+>'.join(prehead),
            '<<<'])
    return head


def run_operation(file_content,stack='',stdin=None,
        stdout=None,footer='>.>>.'):
    """
    This is a function to test arithmetic brainfuck operations
    """

    header = create_header(stack)
    with tempfile.NamedTemporaryFile(mode='w',delete=True) as f:
        f.write(''.join((header,'\n',file_content,footer)))
        f.flush()
        result = subprocess.run(['bf','-c{}'.format(TAPESIZE-1),f.name],
                input=stdin,
                stdout=subprocess.PIPE )
        if stdout:
            return stdout(result.stdout)
        else:
            return int.from_bytes(result.stdout,'big')

