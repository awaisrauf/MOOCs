# Indexing Structures for Files and  Physical Database Design

- if primary file organization exists, then additional auxiliary access structures called indexes can be created to speed up the retrieval
	- indexes are additional files on the disk that provide alternative ways (secondary access paths) to access records without affecting the physical placement of records
	- enable efficient access
	- any field of the record can be used to create an index, multiple indexes on different fields, or indexes on multiple indexes on the same file

## Types of Single-level Ordered Indexes

- **Index**: a file with a given record consisting of multiple fields (attributes), an index is usually defined on a single field called an indexing field
	- the index stores each value of the index field along with a list of pointers to blocks that contain a record with that field
	- the values in the index are ordered to enable binary search
- **Primary Index**: specified on the ordering key field (ordering key field is used to physically order file records on disk, every field has a unique value for the record)
- **Clustering Index**: if the ordering field is not unique for a file. 
- A file can at most have one physical ordering field, so it only has one primary or clustering index
- **Secondary Index**: Specified on the non-ordering field of a file. Data files can have multiple secondary indexes.

### Primary Index

- An ordered file whose records are fixed length with two fields: 
	1. primary key of the data file 
	2. pointer to a disk block 
-  $<K(i), P(i)>$ 
- acts like an access structure 
- An index is a dense index if it has an entry for every search key value in the data file
- Sparse index has entries for only a few search values. 
- the primary index file is much smaller
	- more index entries fit on few blocks and hence require fewer disk block accesses 
	- if an index has $b_i$ blocks, then the binary search would require $\log_2 b_i + 1$ accesses. 

### Clustering Indexes

- if file records are physically ordered on a non-key field (non-distinct)
- each distinct key has one record in the index

### Secondary Index

- provides a secondary means to access a data file for which some primary access already exists
- could be created with unique or non-unique keys, ordering or non-ordering keys
- It is an ordered file with two fields: index field and pointer to block or record pointer
**Example**
- file of records $r=300,000$ fixed length
- size $R=100$ bytes
- stored on a disk of block size $B=4096$
- the file has $b=7500$ bocks
- blocking factor $bfr=ceil(4096/100)=40$
- number of blocks needed for a file $b=floor(r/bfr)=7500$
- for a search with a secondary key (a non-ordering key)
	- average blcoks access = b/2 = 7500/2375
	- for binary search
		- a block pointer is P=6 bytes
		- the field size = 9 bytes
		- blocking factor for secondary index = $ceil(4096/15)=273$
		- number of blocks needed for secondary index = $floor(300000/273)=1099$
		- a binary search for this secondary index would be $floor(log_2 (1099))=11$ blocks access + one additional block access for data = 12 blocks

## Multilevel Indexes

- multilevel indexes create indexes for the primary index to reduce search time by blocking factor
	- searching multi-level index requires approximately $log_{fo} b_i$
	- where $fo$ is fanout factor which is $bfr_i$
- Assumes ordered index file with distinct values and fixed length entries for each $K(i)$. 
	- first level needs $r_i/fo$ which is $r_2$
	- second level index: create an index for the primary index
		- the second level has one entry for each block in the first level
	- similarly creating an index at the third level based on the second-level number of entries in the third level is $r_3=floor(r_2/fo)$

**Example**
- blocking factor $bfr_i=273$ index entreis per block
- fan-out $fo=273$
- number of second-level blocks $b_2=floor(b1/fo)=1099/273=5$
- third number blocks $b_3=floor(b_2/273)=5/273=1$
- hence t=3
- total number of block access = t+1=3+1

## Dynamic Multilevel Indexes Using $B$-Trees and $B^+$-Trees

## Some General Issues Concerning Indexing

-  logical vs. physical indexes. 
	- if physical addresses are stored in the indexes, change in physical address could cause issues
	- a logical index is used which creates one more level of indirection
- 
