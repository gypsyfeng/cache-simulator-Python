import unittest
from cache import Block

class TestBlock(unittest.TestCase):
    '''Test the init, use, write and __eq__ of class Block in cache.py'''
    
    def test_init (self):
        print("------------------------test_block_init------------------------")
        b = Block(32)
        self.assertEqual(b.size, 32)
        self.assertEqual(b.in_use, False)
        self.assertEqual(b.dirty, False)
        self.assertEqual(b.data, [])
        self.assertEqual(b.valid, False)
        
    def test_use(self):
        print("------------------------test_block_use------------------------")
        b = Block(64)
        b.use()
        self.assertEqual(b.size, 64)
        self.assertEqual(b.in_use, True)
        self.assertEqual(b.dirty, False)
        self.assertEqual(b.data, [0]*64)
        self.assertEqual(b.valid, True)
        
    def test_write(self):
        print("------------------------test_block_write------------------------")
        b = Block(32)
        b.use()
        b.write(False)
        self.assertEqual(b.dirty, False)
        b.write(True)
        self.assertEqual(b.dirty, True)
        #write-back write policy
        b.write(False)
        self.assertEqual(b.dirty, True)
        
    def test_eq(self):
        print("------------------------test_block_eq------------------------")
        a = Block(32)
        a.use()
        a.write(True)
        b = Block(32)
        b.use()
        b.write(True)
        self.assertTrue(a == b)
        
def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestBlock)
    
if __name__ == '__main__':
    unittest.main()