import unittest, random
from cache import PageTable, Cache

class TestPageTable(unittest.TestCase):
    '''Test init, write and read of class PageTable in cache.py'''
    
    def test_init(self):
        print("------------------------test_pgt_init------------------------")
        pgt = PageTable(5)
        self.assertEqual(pgt.size, 5)
        self.assertEqual(pgt.table, {0:None, 1:None, 2:None, 3:None, 4:None})
        
    def setUp(self):
        
        self.block_quan = random.randint(2, 20)
        self.size = random.randint(self.block_quan, self.block_quan*5)
        self.pgt = PageTable(self.size)
        self.cache = Cache(self.block_quan*32, 32)
        self.ptes = random.sample(range(self.size), random.randint(2, self.size))
        random.shuffle(self.ptes)
        self.miss_pte = self.ptes.pop()
        
    def tearDown(self):
        
        self.pgt = None
        self.ptes = None
        self.miss_pte = None

    def test_wrtie_hit(self):
        print("------------------------test_pgt_write_hit------------------------")
        for p in self.ptes:
            self.pgt.read(p, self.cache)
        tag = None
        for t in self.cache.tag_list:
            if t[1] != None and self.pgt.table[t[1]] == t[0]:
                    tag = t
                    break
        self.assertIsNotNone(tag)
        self.pgt.write(tag[1], self.cache)
        self.assertEqual(self.pgt.table[tag[1]], tag[0])
        
        
    def test_write_miss(self):
        print("------------------------test_pgt_write_miss------------------------")
        for p in self.ptes:
            self.pgt.read(p, self.cache) 
        for t in self.cache.tag_list:
            if t[1] != self.miss_pte:
                self.pgt.table[self.miss_pte] = t[0]
                break
        self.pgt.write(self.miss_pte, self.cache)
        self.assertIsNotNone(self.pgt.table[self.miss_pte])
        
    def test_read_hit(self):
        print("------------------------test_pgt_read_hit------------------------")
        for p in self.ptes:
            self.pgt.write(p, self.cache)
        tag = None
        for t in self.cache.tag_list:
            if t[1] != None and self.pgt.table[t[1]] == t[0]:
                    tag = t
                    break
        self.assertIsNotNone(tag)
        self.pgt.read(tag[1], self.cache)
        self.assertEqual(self.pgt.table[tag[1]], tag[0])
    
    def test_read_miss(self):
        print("------------------------test_pgt_read_miss------------------------")
        for p in self.ptes:
            self.pgt.write(p, self.cache) 
        for t in self.cache.tag_list:
            if t[1] != self.miss_pte:
                self.pgt.table[self.miss_pte] = t[0]
                break
        self.pgt.read(self.miss_pte, self.cache)
        self.assertIsNotNone(self.pgt.table[self.miss_pte])        
        
        
    def test_read_null_cache(self):
        print("------------------------test_pgt_read_null_cache------------------------")
        with self.assertRaises(AttributeError):
            self.pgt.read(random.randint(0, self.size), None)
    
    def test_write_null_cache(self):
        print("------------------------test_pgt_write_null_cache------------------------")
        with self.assertRaises(AttributeError):
            self.pgt.write(random.randint(0, self.size), None)
    
    def test_write_incorrect_pte(self):
        print("------------------------test_pgt_write_incorrect_pte------------------------")
        pte = random.randint(self.size, self.size*2)
        with self.assertRaises(AttributeError):
            self.pgt.write(pte, random.randint(0, self.block_quan))
        #self.assertRaises(AttributeError, self.pgt.write(pte, random.randint(0, self.block_quan)))
    
    def test_read_incorrect_pte(self):
        print("------------------------test_pgt_read_incorrect_pte------------------------")
        pte = random.randint(self.size, self.size*2)
        with self.assertRaises(AttributeError):
            self.pgt.read(pte, random.randint(0, self.block_quan))
        
def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestPageTable)
                

if __name__ == '__main__':
    unittest.main()
    
    
    
    
    
