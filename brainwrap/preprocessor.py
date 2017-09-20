import re
import subprocess
import sys
"""
This function runs the code through gcc's preprocessor followed by
stripping all non bf characters
"""
def run(bfcode):
    # First run through gcc preprocessor
    preproc = subprocess.run(['cpp'],
            input=bytes(bfcode,'utf-8'),
            stdout=subprocess.PIPE).stdout
    # Bytes to string
    preproc = str(preproc,'utf-8')
    # Strip commented out lines in the proprocessor added by gcc
    preproc = re.sub(r'#.*?\n','',preproc)
    # Strip all non-bf characters
    result = re.sub('[^][<>,.+-]*','',preproc)
    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    print(run(input))

