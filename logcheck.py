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

    def readfile(self, file):
        for line in open(file):
            name = tuple(name for name in self.node_names if name in line)
            if name:
                self.nodes[name[0]].make_log_entry(line)
            else:
                self.nodes['system'].make_log_entry(line)
