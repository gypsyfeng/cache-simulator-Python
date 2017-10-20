import test_block, test_cache, test_page_table, test_simulator, unittest

#combine all the test cases

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    suite1 = test_block.suite()
    suite2 = test_cache.suite()
    suite3 = test_page_table.suite()
    suite4 = test_simulator.suite()
    alltests = unittest.TestSuite([suite1, suite2, suite3, suite4])
    runner.run(alltests)

