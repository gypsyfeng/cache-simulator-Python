class Block:
    '''Block represents '''
    
    def __init__(self, size):
        self.size = size
        self.in_use = False
        self.dirty = False
        self.data = []
        self.valid = False
    
    def use(self):
        self.data = [0] * self.size
        self.in_use = True
        self.valid = True
        self.dirty = False
        
    def write(self, write):
        self.dirty = self.dirty and True or write
        return self
    
    def p(self):
        print ([self.size, self.in_use, self.dirty, self.valid])
        
    def __eq__(self, other):
        
        if other is None:
            return False
        return (self.size, self.in_use, self.dirty, self.valid) == (other.size, other.in_use, other.dirty, other.valid)
        
class PageTable:
    '''PageTable maps a pte (virtual address) to a tag (physical address) in cache'''
    
    def __init__(self, size):
        '''init a page table with maximum size to read from and write to'''
        self.size = size
        self.table = {}
        for i in range(size):
            self.table[i] = None
            
    def write(self, pte, cache):
        '''data in pte is changed and update to cache'''
        self.table[pte] = cache.ref(pte, self.table[pte], True)
        
    def read(self, pte, cache):
        '''read data in pte from cache'''
        self.table[pte] = cache.ref(pte, self.table[pte], False)
        
            
class Cache:
    '''Cache maps a tag to both a pte and a block'''
    
    def __init__(self, cache_size, block_size):
        '''Cache with size cache_size is seperated into cache_size/block_size data blocks with block size block_size'''
        
        self.block_quan = cache_size//block_size
        self.cache_size = cache_size
        self.block_size = block_size
        self.tag_list = []
        self.blocks = []
        for i in range(self.block_quan):
            self.tag_list.append([i, None])
            self.blocks.append(Block(self.block_size))
            
    def ref(self, pte, tag, write=False):
        '''Every time the data of pte is referenced (read/write), this function would be called to update the cache.
        write is set to False as desult
        '''
        tag_l = self.tag_list
        if pte == None:
            return None
        #no cache addr recorded in page table in regard to page table entry
        if tag == None or tag >= self.block_quan:
            b = self.ref_to_new_block(pte)
            b.write(write)
            return self.tag_list[0][0]
        
        for i in range(len(tag_l)):
            #ref data is in the cache
            if tag_l[i][0] == tag and tag_l[i][1] == pte:
                self.tag_list = [tag_l.pop(i)] + tag_l
                self.blocks[self.tag_list[0][0]].write(write)
                return self.tag_list[0][0]
            #ref data not in cache
            elif tag_l[i][0] == tag and tag_l[i][1] != pte:
                b = self.ref_to_new_block(pte)
                b.write(write)
                return self.tag_list[0][0]
            
        return None
                
        
    def ref_to_new_block(self, pte):
        '''helper function for ref()'''
        
        blocks = self.blocks
        tag_list = self.tag_list
        for i in range(self.block_quan):
            if blocks[i].in_use == False:
                blocks[i].use()
                #loop through the tag list from i to left and right simultaneously 
                left, times = i, self.block_quan//2
                right = left+1 < self.block_quan and left+1 or 0
                while times >= 0:
                    if tag_list[left][0] == i:
                        tag_list[left][1] = pte
                        self.tag_list = [tag_list.pop(left)] + tag_list
                        return blocks[i]
                    elif tag_list[right][0] == i:
                        tag_list[right][1] = pte
                        self.tag_list = [tag_list.pop(right)] + tag_list
                        return blocks[i]
                    left -= 1
                    right = right < self.block_quan-1 and right+1 or 0 
                    times -= 1
                
        #evict the lru block
        blocks[tag_list[-1][0]].use()
        tag_list[-1][1] = pte
        self.tag_list = [tag_list.pop(-1)] + tag_list
        return blocks[self.tag_list[0][0]]
        
        