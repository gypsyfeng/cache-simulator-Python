# Python Cache Simulator

Create a cache simulator with a simulated page table. 

Replacement policy: least recently used

Write policy: write back

Unit test and integration test are both included.

## Getting Started

Address is represented by integer. 

**Page Table** - simulate a page table which maps a page table entry (virtual address) to a tag in cache (physical address)

**Block** - represent a data block containing the real data, the status of the block (in_use, dirty, valid), and the size of the block

**Cache** - simulate a lru write-back cache which maps a tag to both a pte and a block with the data from that pte

### Size

Block size is either 32 or 64. 

Cache size is n^2 and it should not be smaller than 64.

Block size is n^2 and it is recommended to be larger than cache size.

### Prerequisites

No extra modules are needed to be installed.

## Run

### Arguments

**cache** - size of the cache, should not be smaller than 64, example: 64, 128, 256, 1025, 8192

**file** - name of the file containing the block size, memory size and page table

### Generate a file with random information

"file1.txt", "file2.txt", "file3.txt" are provided.

If you want to generate a file with random information, use test_utils.gen_simulator_file(cache_size).
Remember to delete the generated file after finish to avoid affecting the test result. 

### Result

A result file will be created after each run. 

The result file records the information of the cache in the final stage, including sizes and the mapping of tags and ptes.

### Example

```
simulator.py 512 "file1.txt"
```

## Running the tests

all tests: test_all.py

unit test: test_block.py, test_cache.py, test_page_table.py

integration test: test_simulator.py


## Authors

 **Yunzhou Feng** 

