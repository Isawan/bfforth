from subprocess import Popen, PIPE
import tempfile
import brainwrap.preprocessor as preprocessor

class BrainfuckMachine:
    def __init__(self,bfcode,tapesize=30000):
        self.code = preprocessor.run(bfcode)
        self.process = Popen(['bff4/bff4'], stdin=PIPE, stdout=PIPE)
        self.process.stdin.write(bytes(self.code+'!','ascii'))
        self.process.stdin.flush()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.stop()

    @property
    def stdin(self):
        return self.process.stdin

    @property
    def stdout(self):
        return self.process.stdout
    
    @property
    def is_running(self):
        return self.process.poll()

    def stop(self):
        self.stdin.close()
        self.stdout.close()

