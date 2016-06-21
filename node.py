class Node:
    def __init__(self, name):
        self.log = []
        self.name = name
        self.count = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.count += 1
        if self.count >= len(self.log):
            raise StopIteration
        else:
            return self.log[self.count][0]

    def make_log_entry(self, line):
        # TODO: make this tuple of tuples
        self.log.append(list(line.split(';')))
