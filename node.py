class Node:
    log = ()

    def __init__(self, name):
        self.name = name

    def make_log_entry(self, line):
        self.log += tuple(line.split(';'))

    def print_log(self):
        for line in self.log:
            print(line)

