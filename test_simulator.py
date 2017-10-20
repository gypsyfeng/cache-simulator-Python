import unittest, random, os
from cache import Cache, PageTable, Block
from test_utils import gen_simulator_file

class TestSimulator(unittest.TestCase):
    '''Test Simulator.py, integration test with different cache sizes'''
    
    def test_cache_64(self):
        print("------------------------Test cache with size 64--------------------------")
        cache_size = 64
        file_name = "cache_64.txt"
        result_file_name = "result_cache_64.txt"
        tag_l = gen_simulator_file(64)
        os.system("python simulator.py 64 %s" % file_name)
        result_f = open(result_file_name, "r")
        self.assertEqual(int(result_f.readline().split()[-1]), 64)
        block_quan = int(result_f.readline().split()[-1])
        self.assertEqual(block_quan*int(result_f.readline().split()[-1]), 64)
        result_f.readline().split()[-1]
        
        for i in range(block_quan):
            self.assertEqual(result_f.readline().split()[1], str(tag_l[i]))
        result_f.close()
        os.remove("cache_64.txt")
        os.remove("result_cache_64.txt")
        
        
    def test_cache_128(self):
        print("------------------------Test cache with size 128--------------------------")
        cache_size = 128
        file_name = "cache_128.txt"
        result_file_name = "result_cache_128.txt"
        tag_l = gen_simulator_file(128)
        os.system("python simulator.py 128 %s" % file_name)
        result_f = open(result_file_name, "r")
        self.assertEqual(int(result_f.readline().split()[-1]), 128)
        block_quan = int(result_f.readline().split()[-1])
        self.assertEqual(block_quan*int(result_f.readline().split()[-1]), 128)
        result_f.readline().split()[-1]
        
        for i in range(block_quan):
            self.assertEqual(result_f.readline().split()[1], str(tag_l[i]))
        result_f.close()
        os.remove("cache_128.txt")
        os.remove("result_cache_128.txt")

    def test_cache_256(self):
        print("------------------------Test cache with size 256--------------------------")
        cache_size = 256
        file_name = "cache_256.txt"
        result_file_name = "result_cache_256.txt"
        tag_l = gen_simulator_file(256)
        os.system("python simulator.py 256 %s" % file_name)
        result_f = open(result_file_name, "r")
        self.assertEqual(int(result_f.readline().split()[-1]), 256)
        block_quan = int(result_f.readline().split()[-1])
        self.assertEqual(block_quan*int(result_f.readline().split()[-1]), 256)
        result_f.readline().split()[-1]
        
        for i in range(block_quan):
            self.assertEqual(result_f.readline().split()[1], str(tag_l[i]))
        result_f.close()
        os.remove("cache_256.txt")
        os.remove("result_cache_256.txt")
        
    def test_cache_512(self):
        print("------------------------Test cache with size 512--------------------------")
        cache_size = 512
        file_name = "cache_512.txt"
        result_file_name = "result_cache_512.txt"
        tag_l = gen_simulator_file(512)
        os.system("python simulator.py 512 %s" % file_name)
        result_f = open(result_file_name, "r")
        self.assertEqual(int(result_f.readline().split()[-1]), 512)
        block_quan = int(result_f.readline().split()[-1])
        self.assertEqual(block_quan*int(result_f.readline().split()[-1]), 512)
        result_f.readline().split()[-1]
        
        for i in range(block_quan):
            self.assertEqual(result_f.readline().split()[1], str(tag_l[i]))
        result_f.close()
        os.remove("cache_512.txt")
        os.remove("result_cache_512.txt")
        
    def test_cache_1024(self):
        print("------------------------Test cache with size 1024--------------------------")
        cache_size = 1024
        file_name = "cache_1024.txt"
        result_file_name = "result_cache_1024.txt"
        tag_l = gen_simulator_file(1024)
        os.system("python simulator.py 1024 %s" % file_name)
        result_f = open(result_file_name, "r")
        self.assertEqual(int(result_f.readline().split()[-1]), 1024)
        block_quan = int(result_f.readline().split()[-1])
        self.assertEqual(block_quan*int(result_f.readline().split()[-1]), 1024)
        result_f.readline().split()[-1]
        
        for i in range(block_quan):
            self.assertEqual(result_f.readline().split()[1], str(tag_l[i]))
        result_f.close()
        os.remove("cache_1024.txt")
        os.remove("result_cache_1024.txt")
        
    def test_cache_2048(self):
        print("------------------------Test cache with size 2048--------------------------")
        cache_size = 2048
        file_name = "cache_2048.txt"
        result_file_name = "result_cache_2048.txt"
        tag_l = gen_simulator_file(2048)
        os.system("python simulator.py 2048 %s" % file_name)
        result_f = open(result_file_name, "r")
        self.assertEqual(int(result_f.readline().split()[-1]), 2048)
        block_quan = int(result_f.readline().split()[-1])
        self.assertEqual(block_quan*int(result_f.readline().split()[-1]), 2048)
        result_f.readline().split()[-1]
        
        for i in range(block_quan):
            self.assertEqual(result_f.readline().split()[1], str(tag_l[i]))
        result_f.close()
        os.remove("cache_2048.txt")
        os.remove("result_cache_2048.txt")
        
    def test_cache_4096(self):
        print("------------------------Test cache with size 4096--------------------------")
        cache_size = 4096
        file_name = "cache_4096.txt"
        result_file_name = "result_cache_4096.txt"
        tag_l = gen_simulator_file(4096)
        os.system("python simulator.py 4096 %s" % file_name)
        result_f = open(result_file_name, "r")
        self.assertEqual(int(result_f.readline().split()[-1]), 4096)
        block_quan = int(result_f.readline().split()[-1])
        self.assertEqual(block_quan*int(result_f.readline().split()[-1]), 4096)
        result_f.readline().split()[-1]
        
        for i in range(block_quan):
            self.assertEqual(result_f.readline().split()[1], str(tag_l[i]))
        result_f.close()
        os.remove("cache_4096.txt")
        os.remove("result_cache_4096.txt")
        
    def test_cache_8192(self):
        print("------------------------Test cache with size 8192--------------------------")
        cache_size = 8192
        file_name = "cache_8192.txt"
        result_file_name = "result_cache_8192.txt"
        tag_l = gen_simulator_file(8192)
        os.system("python simulator.py 8192 %s" % file_name)
        result_f = open(result_file_name, "r")
        self.assertEqual(int(result_f.readline().split()[-1]), 8192)
        block_quan = int(result_f.readline().split()[-1])
        self.assertEqual(block_quan*int(result_f.readline().split()[-1]), 8192)
        result_f.readline().split()[-1]
        
        for i in range(block_quan):
            self.assertEqual(result_f.readline().split()[1], str(tag_l[i]))
        result_f.close()
        os.remove("cache_8192.txt")
        os.remove("result_cache_8192.txt")

def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestSimulator)
        

if __name__ == '__main__':
    unittest.main()