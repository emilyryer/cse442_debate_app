import unittest
import logging
import comments
import os

class TestComments(unittest.TestCase):

    def setUp(self):
        open('base_trees.txt', 'w').close() #create file with no base comments

    def tearDown(self):
        os.remove('base_trees.txt') #deletes the file so not used in other tests

    def test_createComment_no_base(self):
        logging.info('STARTING CREATE COMMENT NO BASE TEST')
        comments.createComment(None, 'foo')
        comments.createComment(None, 'bar')
        bases = []
        with open('base_trees.txt', 'r') as f:
            for line in f:
                bases.append(line.strip('\n'))
        self.assertEqual(bases[0], 'base1')
        self.assertEqual(bases[1], 'base2')
        f.close()

if __name__ == '__main__':
    unittest.main()
