import unittest
from logcheck import LogCheck


class Tests(unittest.TestCase):
    def test_setup_node_objects(self):
        l = LogCheck()
        for name in ('comp001', 'comp147'):
            self.assertIn(name, l.node_names)

if __name__ == '__main__':
    unittest.main()
