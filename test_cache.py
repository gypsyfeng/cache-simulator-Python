import unittest
import random
from cache import Cache
from test_utils import *

class TestCache(unittest.TestCase):
    '''Test the init and ref of class Cache in cache.py'''
    
    def setUp(self):
        
        self.block_size = 32
        self.cache_size = random.choice([2**i for i in range(5, 14)])
        self.cache = Cache(self.cache_size, self.block_size)
        self.read_block = Block(32)
        self.read_block.use()
        self.write_block = Block(32)
        self.write_block.use()
        self.write_block.write(True)
        
    def tearDown(self):
        
        self.cache = None
    
    def test_init(self):
        print("------------------------test_cache_init------------------------")
        c = Cache(128, 32)
        bl = Block(32)
        tl = [[i, None] for i in range(4)]
        self.assertEqual(c.block_quan, 4)
        self.assertEqual(c.cache_size, 128)
        self.assertEqual(c.block_size, 32)
        self.assertEqual(c.tag_list, tl)
        for b in c.blocks:
            self.assertTrue(b == bl)
 
        
    def test_ref_defualt_write(self):
        print("------------------------test_cache_ref_defualt_write------------------------")
        i = self.cache.ref(3, None)
        self.assertEqual(self.cache.blocks[i].dirty, False)
    
    def test_ref_full_cache_miss(self):
        print("------------------------test_cache_ef_full_cache_miss------------------------")
        self.cache, pte = full_cache_miss(self.cache)
        b = self.cache.ref(pte, random.randint(0, self.cache.block_quan), False)
        self.assertTrue(self.cache.blocks[b] == self.read_block)
        self.assertEqual(self.cache.tag_list[0], [b, pte])
    
    def test_ref_full_cache_hit(self):
        print("------------------------test_cache_ref_full_cache_hit------------------------")
        self.cache, tag = full_cache_hit(self.cache)
        write = self.cache.blocks[tag[0]].dirty
        b = self.cache.ref(tag[1], tag[0], False)
        if write:
            self.assertTrue(self.cache.blocks[tag[0]] == self.write_block)
        else:
            self.assertTrue(self.cache.blocks[tag[0]] == self.read_block)
        self.assertEqual(tag, self.cache.tag_list[0])
        
    def test_ref_not_full_cache_miss(self):
        print("------------------------test_cache_ref_not_full_cache_miss------------------------")
        self.cache, pte = not_full_cache_miss(self.cache)
        b = self.cache.ref(pte, random.randint(0, self.cache.block_quan), True)
        self.assertTrue(self.cache.blocks[b] == self.write_block)
        self.assertEqual(self.cache.tag_list[0], [b, pte])        
        
        
    def test_ref_not_full_cache_hit(self):
        print("------------------------test_cache_ref_not_full_cache_hit------------------------")
        self.cache, tag = not_full_cache_hit(self.cache)
        b = self.cache.ref(tag[1], tag[0], True)
        self.assertTrue(self.cache.blocks[tag[0]] == self.write_block)
        self.assertEqual(tag, self.cache.tag_list[0])        
        
    def test_ref_empty_cache_null_tag(self):
        print("------------------------test_cache_ref_empty_cache_null_tag------------------------")
        pte = random.randint(0, 100)
        b = self.cache.ref(pte, None, True)
        self.assertTrue(self.cache.blocks[0] == self.write_block)
        self.assertEqual(self.cache.tag_list[0], [0, pte])
        
    def test_ref_null_pte(self):
        print("------------------------test_cache_ref_null_pte------------------------")
        self.assertEqual(self.cache.ref(None, 4, False), None)
        
    
def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestCache)
        

if __name__ == '__main__':
    unittest.main()

    
    
    