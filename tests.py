import unittest
from logcheck import LogCheck


class Tests(unittest.TestCase):
    def test_setup_node_objects(self):
        l = LogCheck()
        self.assertIn('comp001', l.node_names)
        self.assertIn('comp147', l.node_names)

if __name__ == '__main__':
    unittest.main()
