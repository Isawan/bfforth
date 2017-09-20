from subprocess import Popen, PIPE
import tempfile
import brainwrap.preprocessor as preprocessor

class BrainfuckMachine:
    def __init__(self,bfcode,tapesize=30000):
        self.code = preprocessor.run(bfcode)
        self.tapesize = tapesize

        self.file = tempfile.NamedTemporaryFile(mode='r+',delete=True)
        self.file.write(self.code)
        self.file.flush()
        self.file.seek(0)
        self.process = Popen(['bf','-c{}'.format(self.tapesize-1),self.file.name],
                stdin=PIPE,
                stdout=PIPE)

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
        self.file.close()
        self.stdin.close()
        self.stdout.close()

