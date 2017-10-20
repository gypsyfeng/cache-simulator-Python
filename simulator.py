import random, argparse, string
from cache import Cache, PageTable

c = None

def main():

    parser = argparse.ArgumentParser(description='Simulate a cache with least \
    recently used replacement policy.')
    
    parser.add_argument("cache", type=int, help = "Size of cache in bytes")
    parser.add_argument("file", type=str, help = 'Name of the file loggin the \
    memory size and the actions of accessing data')
    
    args = parser.parse_args()
    
    cache_size = args.cache
    f = open(args.file, 'r')
    memory_size = int(f.readline().split()[-1])
    block_size = int(f.readline().split()[-1])
    
    pgt = PageTable(memory_size//block_size)
    cache = Cache(cache_size, block_size)
    
    for line in f.readlines():
        l = line.split()
        action, pte = l[0], int(l[1])
        if action == 'write':
            pgt.write(pte, cache)
        elif action == 'read':
            pgt.read(pte, cache)
            
    #create a result file
    result_file = "result_cache_%i.txt" % cache_size
    f = open (result_file, "w+")
    f.write("cache size: %i\n" % cache.cache_size)
    f.write("block quantity: %i\n" % cache.block_quan)
    f.write("block size: %i\n" % cache.block_size)
    f.write("tag pte\n")
    for t in cache.tag_list:
        if t[1] == None:
            f.write("%d None\n" % t[0])
        else:
            f.write("%d %d\n" % (t[0], t[1]))
    f.close()
    
if __name__ == '__main__':
    main()
    
        
        