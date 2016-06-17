class Node:
    log = []

    def __init__(self, name):
        self.name = name

    def make_log_entry(self, line):
        # TODO: make this tuple of tuples
        self.log.append(list(line.split(';')))

    def print_log(self):
        for line in self.log:
            print(line[0], line[5])
