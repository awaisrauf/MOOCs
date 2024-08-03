# Chapter 14 - Basics of Functional Dependencies and Normalization for Relational Databases

- The formal way of analyzing why the grouping of attributes into a relation schema may be better than another
- Here, measure formally why one set of groupings of attributes into relation schemas is better than other
- Two levels for the goodness of relation schema
	- logical (conceptual): how users interpret the relation schemas and meaning of attrs
	- implementaiton (physical storage)
- two design approaches: bottom-up and top-down
- relational database design ultimately produces a set of relations
	- the implicit goal: information preservation and minimum redundancy
## Informal Design Guidelines for Relation Schemas

- Four informal guidelines that may be used to determine the quality of relation schema design
	1. make sure the semantics of attributes are clear in the schema
	2. reducing the redundant information in tuples
	3. reducing the NUL values in tuples
	4. disallowing the possibility of generating spurious tuples
### Imparting Clear Semantics

> The ease with which the meaning of a relation’s attributes can be explained is an informal measure of how well the relation is designed.

#### Guideline 1
- design a schema so that it's easy to explain its meaning
	- do not mix attributes from multiple entity types into a single relation
	- it is easy to explain a relation schema if it corresponds to one entity type or relationship
### Redundant Information in Tuples and Update Anomalies

- One goal is to minimize storage space so avoid repeating attributes
- Storing natural joins of base relations can lead to additional problems referred to as update anomalies
	- **Insertion Anomalies**: 
	- **Deletion Anomalies**: 
	- **Modification Anomalies**:
#### Guideline 2
- design database such that insertion, deletion, and modification anomalies do not exist. If anomalies are present, make sure to make them clear so that programs that update them can operate correctly
### NULL Values in Tuples
NULL is 
- waste of storage space
- lead to problems in understanding the meaning of an attribute
- problems with JOIN statements at the logical level
- how to account it for aggregate functions (COUNT, SUM)
- NULL can have multiple interpretations 
	- does not apply
	- value unknown
	- known but absent
#### Guideline 3
- Avoid placing attributes in base relation whose value may be NULL frequently 
- separate relation for those columns which may have many NULL
	- for instance, if only 15% of employees will have personal offices, create a separate table for it
### Generation of Spurious Tuples
#### Guideline 4
- Design relation schema so that they can be joined with equality conditions on attributes that are appropriately related (primary key, foreign key) pairs in a way that guarantees that no spurious tuples are generated
- Avoid relations that contain matching attributes that are not (foreign key, primary key) combinations because they create spurious tuples when joined
## Functional Dependencies 
- a formal analysis tool
### Definition of Functional Dependency 

- constraint between two sets of attributes from the database
- Suppose our database schema has $n$ attributes $A_1, A_2, ..., A_n$ described by the single universal schema $R=\{A_1, ..., A_n\}$. 
- Definition: 
	- A functional dependency denoted $X\to Y$ between to attributes $X$ and $Y$ that are subsets of $R$ specifies a constraint on the possible tuples that can form a relation state r of $. 
	- Constraint is that for any two tuples that have t1[X]=t2[X] also t1[Y]=t2[Y]
- In other words, values of the Y component of a tuple r depend on the determined values of the X component
> We also say that there is a functional dependency from X to Y

- functional dependency defines how attributes relate to each other 
- are property of relation schema $R$ not of particular legal relation state
> Given a populated relation, we cannot determine which FDs hold and which do not
unless we know the meaning of and the relationships among the attributes
- however, we can state that an FD does not hold if there is a clear violation of such an FD
## Normal Forms Based on Primary Keys
- Assume that 
	-  a set of functional dependencies is given for each relation 
	- each relation has a designated primary key
### Normalization of Relations 
- normalization process takes a relation schema through a series of tests to certify whether it satisfies  a certain normal form
- Four normal forms (1NF, 2NF, 3NF, BCNF) are based on functional dependencies among attributes of a relation
- Normalization of data: the process of analyzing given relation schema based on their FDs and primary keys to achieve the desirable properties of 
	- minimizing redundancy 
	- minimizing insertion, deletion, and update anomalies
> It can be considered as a “filtering” or “purification” process to make the design have successively better quality.
- a relation schema that does not meet the condition for a normal form is decomposed into a smaller subset of attributes-based schemas
Normal form: degree to which a relation has been normalized

- Normalization alone does not guarantee good schema design, rather normalization through decomposition must also confirm the existence of additional properties that the schema has
	- nonadditive join or lossless join property: no spurious tuples generation issue with join
	- dependency preservation property: each functional dependency is represented in some individual relation  resulting after decomposition 
- Normalization up to 3NF, BCNF, or at most 4NF is enough
- database designer need not normalize to the highest possible normal form

#### Definitions
 - **Superkey**: a set of attributes $S\subseteq R$ with a property that no two tuples t_1 and t_2 in any legal state are $t_1[S]=t_2[S]$
 - the **key** is superkey with the addition that removal of any attribute from K will cause K to not be a superkey
	 > {Ssn} is a key for EMPLOYEE, whereas {Ssn}, {Ssn, Ename}, {Ssn, Ename, Bdate}, and any set of attributes that includes Ssn are all superkeys.
	 
### First Normal Form
- the domain of attributes must include only atomic and indivisible values 
- value of any attribute in a tuple must be a single value from the domain of attributes
	- no relation within relations
	- no set of values
	- no tuple ofvlaues or combination 
- Three ways to achieve 1NF for xxx
	1. remove an attribute that violates 1NF and place it in a separate relation. 
	2. Expand the key so that there will be a separate tuple in the original and the primary key will be a combination of the original and new attribute
	3. if the maximum number of values is known for the attribute, then remove that attribute and replace it with the maximum number of attributes 
- 1NF also disallows multivalued attributes that are themselves composite 

### Second Normal Form