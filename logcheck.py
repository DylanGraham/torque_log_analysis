import re
from node import Node

work_dir = '/home/dylan/Downloads/pbs_server_logs/'
file_name = '20150212'
node_name = 'comp079'


class LogCheck:
    def __init__(self):
        self.nodes = []

    def readfile(self, file):
        for line in open(file):
            if re.search(node_name, line):

                if node_name not in self.nodes:
                    x = Node(node_name)
                    x.make_log_entry(line)
                    self.nodes.append(x)
                else:
                    self.nodes.append(line)

l = LogCheck()
l.readfile(work_dir + file_name)
for node in l.nodes:
    node.print_log()


