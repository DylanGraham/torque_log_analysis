class Node:
    def __init__(self, name):
        self.log = []
        self.name = name

    def __iter__(self):
        self.index = -1
        return self

    def __next__(self):
        self.index += 1
        if self.index >= len(self.log):
            raise StopIteration
        else:
            return self.log[self.index][0]

    def make_log_entry(self, line):
        self.log.append(list(line.split(';')))
