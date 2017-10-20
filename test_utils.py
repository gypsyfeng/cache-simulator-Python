import random
from cache import Cache, PageTable, Block

def full_cache_hit(cache):
    
    size = cache.block_quan
    pt_size = size*random.randint(1,5)
    ptes = random.sample(range(pt_size), size)
    for i in range(size):
        cache.tag_list[i][1] = ptes[i]
        cache.blocks[i].use()
        cache.blocks[i].write(random.choice([True, False]))
    random.shuffle(cache.tag_list)
    tag = random.choice(cache.tag_list)
    return cache, tag

def full_cache_miss(cache):
    
    size = cache.block_quan
    pt_size = size*random.randint(2,5)
    ptes = random.sample(range(pt_size), size+1)
    pte = ptes[-1]
    for i in range(size):
        cache.tag_list[i][1] = ptes[i]
        cache.blocks[i].use()
        cache.blocks[i].write(random.choice([True, False]))
    random.shuffle(cache.tag_list)
    return cache, pte

def not_full_cache_hit(cache):
    
    size = cache.block_quan
    not_full_size = random.randint(1, size-1)
    pt_size = size*random.randint(1,5)
    ptes = random.sample(range(pt_size), not_full_size)
    for i in range(not_full_size):
        cache.tag_list[i][1] = ptes[i]
        cache.blocks[i].use()
        cache.blocks[i].write(random.choice([True, False])) 
    tag = random.choice(cache.tag_list[:not_full_size])
    random.shuffle(cache.tag_list)
    return cache, tag

def not_full_cache_miss(cache):
    
    size = cache.block_quan
    not_full_size = random.randint(0, size-1)
    pt_size = size*random.randint(1,5)
    ptes = random.sample(range(pt_size), not_full_size+1)
    pte = ptes[-1]
    for i in range(not_full_size):
        cache.tag_list[i][1] = ptes[i]
        cache.blocks[i].use()
        cache.blocks[i].write(random.choice([True, False]))
    random.shuffle(cache.tag_list)
    return cache, pte

def gen_simulator_file(cache_size):
    
    #make sure cache size here is larger than 64
    f = open("cache_%s.txt" % str(cache_size), "w+")
    block_size = random.choice([32, 64])
    block_quan = cache_size//block_size
    pgt_size = random.randint(block_quan, block_quan*5)
    memory_size = pgt_size*block_size
    total_actions_times = random.randint(0, pgt_size*3)
    
    f.write("memory size: %s\n" % str(memory_size))
    f.write("block size: %s\n" % str(block_size))
    
    cache_tags = [None for i in range(block_quan)]

    for i in range(total_actions_times):
        pte = random.randint(0, pgt_size-1)
        f.write(random.choice(["read ", "write "]) + str(pte) + "\n")
        try:
            cache_tags.remove(pte)
        except ValueError:
            cache_tags.pop(-1)
        cache_tags = [pte] + cache_tags
    
    f.close()
    return cache_tags

gen_simulator_file(256)
gen_simulator_file(8192)
gen_simulator_file(2048)