from node import Node


class LogCheck:
    def __init__(self):
        self.node_names = []
        self.nodes = {'system': Node('system')}
        self.setup_node_objects()

    def setup_node_objects(self):
        num_nodes = [format(x, '03d') for x in range(174)]
        self.node_names = ["comp" + str(i) for i in num_nodes]
        for n in self.node_names:
            self.nodes[n] = Node(n)

    def name_in_line(self, line):
        for name in self.node_names:
            if name in line:
                yield name

    def readfile(self, file):
        for line in open(file):
            for name in self.name_in_line(line):
                if name:
                    self.nodes[name].make_log_entry(line)
                else:
                    self.nodes['system'].make_log_entry(line)
