# Chapter 16 - Disk Storage, Basic File Structures, Hashing, and Modern Storage Architectures

- Organization of databases in storage and techniques to access them
  
## Introduction

- DB data is stored physically and then can be retrieved by DBS software. 
- Computer storage media form a storage hierarchy:
	- **Primary Storage**: storage media that can be operated by CPU directly: computer memory or cache. 
		- smaller but fast
		- expensive 
		- loses when power is cut off
	- **Secondary storage**: SSD, magnetic disks, flash memory
	- **Tertiary storage**: Optical disks (CD-ROMs, DVDs, etc) are removable media used in today's systems as offline storage for archiving databases
		- larger capacity
		- costs less 
		- slower access
- data in secondary and tertiary can NOT be processed by CPU directly, first copied into primary storage
  
### Memory Hierarchies and Storage Devices

- levels of memory
	- **cache memory** (static RAM): The CPU uses it to speed up program instructions 
	- **DRAM** (Dynamic RAM) or Main memory: main work for COUP to keep program instructions and data. It has a lower speed than SRAM but cheaper
	- **Flash Memory**: nonvolatile, high density, high performance, electrically erasable programmable read-only memory. two types: NAND and NOR flash-based. Flash USB sticks are a common example
	- **Magnetic Disks**
	- **Optical Drives** CD has 700MB, DVD, 4-15GB. 
		- CD-ROMs are pre-recorded, can not be overwritten
		- CD-R (recordable), DVD-R, DVD-R+: write-once-read-many a form of optical storage used for archiving data. Writing once and read any number of times without erasing. 
			- half GB per disk and last much longer than magnetic disks
			- slower transfer rates
		- Blu-ray DVD: store 27GB per layer
		- Optical jukebox memories: with multiple CD_ROM platters
	- **Magnetic Tapes**: least expensive. used for archiving and backup storage. Tape jukeboxes, a bank of tapes that are cataloged can be used
- Depending on the memory available, a whole or part of DBS can be placed in it. 
- ![[24.png]]
  
### Storage Organization of Databases

- DBS data is persistent data as needs to be stored for long periods of time
- non-volatile storage
- less costly 
- SSDs are a viable alternative to magnetic disks
- Magnetic tapes are frequently used as storage and backup mechanisms for databases as tapes cost less than storage on disk
	- magnetic disks are offline as the operator needs to load them
	- disks are online devices
- Physical database design needs to be organized on a physical medium
- Typically database application needs a smaller portion of data, when a certain portion is needed, 
	- it must be located on the disk
	- copied in the memory
	- rewritten back to disk if needed
- Data stored is organized as files of records, each record is a collection of a record of values 
- several primary file organizations, determining how records are physically placed on disk
	- heap field (unordered file), 
	- sorted (sequential): keeps record order by value of particular field (sort key)
	- hashed file: determines the record's place on disk based on a hash function
- Secondary organization (auxiliary access structure): provides efficient access to file records based on alternate fields (indexes)

## Secondary Storage Devices

### Hardware Description of Disk Devices

- used for large amounts of data storage, a device that handles the disk is a hard disk drive (HDD)
- The basic unit of data: single-bit
	- magnetize an area on disk in certain ways and make that area represent a bit in 0 or 1
	- bits are grouped into bytes (8 bits)
	- capacity: byte it can store
- disks are made of
	- magnetic material shaped as a circular disk
	- protected by plastic or acrylic cover
	- single or double-sided based on the sides it uses for storage of data
	- disk packs have multiple disks to increase capacity![[25.png]]
	- Info stored on disk surface in concentric circles of small diameter called tracks
		- tracks with the same diameter on various surfaces called cylinders. Information on the same cylinder can be accessed fast
		- number of tracks: few 1000s to 152,000
		- each track has tens of kBs
		- each track is divided into smaller blocks or sectors
		- division of tracks into sectors is hard-coded
		- one sector size is 512B![[26.png]]
- **Blocks:** The division of track into equal-sized blocks (or pages) is set by the operating system during disk formatting (or initialization)
	- can not be changed dynamically
	- size ranges from 512 to 8192
	- a disk with hardcoded sectors often has the sectors subdivided or combined into blocks during initialization 
	- blocks are separated by fixed interblock gaps which contain coded control information added during initialization 
		- gaps code used to determine which block on the track follows each interblock gap 
- a disk is a random access addressable device and the transfer of data between main memory and disk takes place in units of disk blocks
	- hardware address of a block is a combination of
		- cylinder number 
		- track number 
		- block number 
	- supplied to disk I/O hardware
	- in many modern drives, a single number called LBA (logical block address) is mapped automatically to the right block
		- number between 0, n
	- The address of a buffer is also provided to disk I/O hardware
		- buffer: a contiguous reserved area in the main storage that holds one disk block
	- For a read command
		- disk block is copied into the buffer
	- for write command 
		- contents of the buffer are copied into the disk block
	- for several contiguous blocks to be copied, the buffer size is adjusted
- Disk drive 
	- a disk or disk pack is mounted on the disk drive
	- the disk drive has a motor that moves 
	- a read/write head includes an electronic component attached to a mechanical arm 
	- disk packs with multiple surfaces are controlled by several read/write heads
	- arms are connected to an actuator connected with a motor which movies it to adjust to the right track
	- Disk drives rotate the disk pack at a constant speed
- A disk controller embedded in the disk drive controls the disk drive and interfaces it computer system
	- SCSI and SATA, SAS are standard interfaces
- the controller accepts high-level I/O commands and takes appropriate actions to position the arm and causes the read/write action to take place
- Total time to locate and transfer an arbitrary block, given address = seek time + rotational delay + block transfer time
	- SEEK TIMe: the time required for the disk controller to mechanically position the read/write head on the correct track
	- rotational delay or latency: desired block moving into the right position. depends on RPMS. For instance, at 15k rpm, time per rotation is 4 msec and average. rotational delay is time per half revolution or 2msec
	- some additional time is required to transfer data called block transfer time
	
 > To make the transfer of multiple blocks more efficient, it is common to transfer several consecutive blocks on the same track or cylinder. This eliminates the seek time and rotational delay for all but the first block and can result in a substantial saving of time numerous contiguous blocks are transferred
 
- seek and rotational time is much larger than block transfer time. 
- transfer time is considered higher compared with the time required to process data in the main memory by the current CPU, hence this is a major bottleneck
- file structure introduced next attempt to minimize the number of block transfers needed to locate and transfer the required data from disk to main memory
- placing related information on contiguous blocks is the basic goal of storage organization on disk

### Making Data Access More Efficient on Disk

1. Buffering of data: new data is held in buffer while old data is being processed
2. the proper organization of data on disk: keeping related data on contiguous blocks
3. Reading data ahead of request: when a block is read into the buffer, blocks from the rest of the track are also copied into the buffer although they are not requested yet
4. Proper scheduling of I/O requests: schedule arm movement in only one direction by arranging data in that way
5. USe of log disks to temporarily hold writes: have logs of writing and do them together 
6. Use of SSDs or flash memory for recovery purposes. 

## Solid State Drives

- Use flash memories between main memory and secondary storage (HDDs)
- Consists of a controller and a set of interconnected flash memory cards, the use of NAND flash memory is most common. 
- no restriction on the order of data since any address is directly accessible
- more expensive compared with HDDs
- DRAM-based SSDs are also available. faster, costlier, and required an internal battery
### Magnetic Tape Storage Devices

- Disks are random access as an arbitrary disk block can be accessed at random
- Magnetic tapes are sequential access devices as you have to access all the preceding blocks before accessing nth block
- Data is stored on reels of high-capacity magnetic tape
- Due to its sequential nature, tapes are not used for online storage but used for backup up data
## Buffering of Blocks
- When several blocks need to be transferred from disk to main memory and their addresses are known, 
	- several buffers can be reserved in the main memory to speed up. 
	- when one buffer is being read or written, the CPU can work on the other one
	- This parallel execution is possible because an independent disk controller exists 
- reading and processing can be done in parallel when the time required to process a disk block in memory is less than the time required to read the next block and fill a buffer. ![[27.png]]
- Double buffering permits the reading or writing of data on consecutive disk blocks 
	- eliminates seek time and rotational delays for all but the first block transfer

### Buffer Management

#### Buffer Management and Replacement Strategies

## Replacing File Records on Disk

- data in the database is a set of records organized as a set of files
  
### Records and Record Types

- data is stored in the form of records, each recording consists of a collection of related data values or items
	- each value is formed of one or more bytes and corresponds to a particular field of the record
- a collection of file names and their corresponding data types constitute record type or record format 
- data type specifies the field of a certain data type based on data type in programming (numeric, int, floating point). E.g., an Employee record type may be defined as a struct in the C programming lang
```c
struct employee {
	char name[30];
	char ssn[9];
	int salary;
	int job_code;
	char department[20];
};
```
- BLOB data are stored separately from its record  in a pool of disk blocks
  
### Files, fixed-length records, and Variable Length Records

- a file is a sequence of records of fixed-length or variable.
- for variable-length records, special separating space can be used to identify their end
- Variable-length records are more complex compared with fixed-length
  
### Record Blocking and Spanned versus Unspanned Records

- records of files must be allocated to disk blocks because the block is a unit of data transfer between disk and memory
- if the block size is large, each block may contain multiple records, measured by the blocking factor
	 $bfr = \text{floor}(B/R)$
	 where
	- $B$ is block size
	- $R$ is the size of fixed length record
- Some space if left as B may not be divided exactly: $B-(bfr*R)$ bytes
	- **Spanned** this unused space can be used by placing part of the next record and a pointer at the end of the first block points to the block containing the rest of the record
	- **Unspanned**: if records are not allowed to cross block boundaries![[28.png]]
- number of blocks needed for a file of $r$ records
	$b = ceil(r/bfr)$

## Operations on Files

- two types: retrieval and update
- Search conditions are simplified by DBMS to extract a simple condition that can be used to locate the records on the disk
	- reach located record is then tested according to the condition
- Operations for locating and accessing file records
	1. **Open**: prepare the file for reading or writing
		- allocate appropriate buffers to hold file blocks from the disk
		- retrieve file header
		- set the file pointer to the beginning of the file
	2. **Reset**: Sets the file pointer of an open  file to the beginning of the file 
	3. **Find (or Locate)**: search for the first record that satisfies the condition
		- transfers block containing that record into a main memory buffer
		- file pointer points to the record in the buffer and becomes the current record
	4. **Read or Get**: Copies the current record from buffer to program variable in the user program
		- may also advance the current record pointer
	5. **FindNext**: Searches for the next record in the file that satisfies the condition
		- transfer block containing that record into a main memory buffer
	6. **Delete**: delete current record, update file on disk
	7. **Modify**: modified some values of the current record, and updated it on the disk
	8. **Insert**: Insert a new file in the record
	9. **Close**: complete file access 
- Several different ways are possible to organize records of a file on a disk

## Files of Unordered Records (Heap Files)

- records are inserted at the end of the file, in the order they arrive
	- inserting is very efficient: the last disk block of the file is copied into the buffer, the new record is added, the block is rewritten back to disk, address of the last file block is kept in the file header
	- searching is linear (b/2 on average)
	- for deleting, the program must find a block, copy it into the buffer, delete it in the buffer, and rewrite the block back to the disk
		- space can be left unused 
		- another way is to use a deletion marker, a byte of whether a record has been deleted or not
- for files of unordered fixed-length records using unspanned and contiguous allocation, 
	- it is straightforward to access them by their position
  
## Files of Ordered Records (Sorted Files)

- records physically ordered by one of their fields
	- reading in the order of ordering a key is extremely efficient
	- ordered files are blocked on contiguous cylinders to minimize seek time
- does not provide benefits for non-ordering fields
- insertion and deletion are expensive as records need to remain physically ordered

## Hashing Techniques

- a hash function (randomization function), which when applied to the field value of a record, gives back the address of the disk block in which the record is stored.
  
### Internal Hashing

- implemented as a hash table through the use of an array of records
	- array index (0 to M) correspond to addresses
	- the hash function applied on the hash value returns the array index on which the record is stored h(K) = K mod M. 

### External Hashing for Disk Files

- hashing for disk files
	- storage space is made up of buckets
	- each bucket consisting of one or more blocks
	- a hash function maps a key into a relative bucket number
	- a table in the file header converts the bucker number into the corresponding disk block address
- hashing provides the fastest possible access for retrieving an arbitrary record given the value of its hash filed

## Other Primary File Organizations

- If two records are related, one record holds a connecting field
- physically, related records are clustered together
