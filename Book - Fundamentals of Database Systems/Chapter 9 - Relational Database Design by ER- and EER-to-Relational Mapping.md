# Chapter 9 - Relational Database Design by ER- and EER-to-Relational Mapping

## Relational Database Design Using ER-to-Relational Mapping

### ER to Relational Mapping Algorithm
- Assume that mapping will create tables with simple single-valued attributes

![[Book - Fundamentals of Database Systems/imgs/7.png]]
![[23.png]]

#### Step 1: Mapping of Regular Entity Types

- For all the regular (strong) entity types E in the ER diagram, create a relation R that includes all the simple attributes
	- include only simple components of composite attributes
	- Choose one of the key attributes of E as the primary key for R
	- If the chosen key is composite, then a set of all simple attributes will act as the primary key
	- if multiple keys were identified, other keys are defined with UNIQUE
- **EXAMPLE**: 

#### Step 2: Mapping of Weak Entity Types

- For each week entity type (W) with owner E in the ER, create relation R that 
	- includes all the simple attributes of W as attributes of R
	- **Identifying relation**: make the owner's (R) key attribute serve as a foreign key attribute of W 
- The cascade option can be chosen for referential triggered action on the foreign key in the relation corresponding to the weak entity types

#### Step 3: Mapping of Binary 1:1 Relationship Types

- For each binary 1:1 relation type R, identify the relations S and T participating in R (e.g., in the example MANAGES). Three approaches
	- **Foreign Key Approach**: Choose one of the relations (e.g., S) and include the primary key of T as the foreign key in the S.
		- include all the simple attributes of R as attributes of S. 
	- **Merged relation approach**: merge two entity types and relationships into one relation. possible when both entities have the same number of tuples all the time
	- **Cross-reference or relationship relation approach**: set up their relation R to cross-reference the primary key of the two relationships S and T. It has the drawback of extra relation and requiring extra join operations when combining related tuples
  
#### Step 4: Mapping of Binary 1:N Relationship Types

Two approaches (foreign key and cross-reference) first approach is preferred. 
- **Foreign key approach**: for 1:N relationship type R, identify the relation S that represents entity type at the N-side
	- include a primary key of T as a foreign key in the S
- **Relationship relation approach**: another approach is to use relationship relation (cross-reference)
	- create a separate relation R whose attributes are primary keys of S and T, which will also be foreign keys of S and T. 
  
#### Step 5: Mapping of Binary M: N Relationship Types

- For an M: N relations type R, create a new relation S to represent R. 
	- the key attributes of participating relations will become a foreign key attribute
	- the combination of these two will form the primary key
- Propagate option for referential triggered action should be specified for foreign keys in the relation as the existence dependency of R is

#### Step 6: Mapping of Multivalued Attributes

- for each multivalued attribute A, create a new relation R. 
	- the relation R will include an attribute corresponding to A
	- the primary key of relation that represents the attribute as the foreign key of R
- referential triggered action should be specified on the foreign key in relation named R 

#### Step 7: Mapping of N-ary Relationship Types

- For each n-ary relationship type R
	- create a new relation S to represent R
	- the primary key of the relations that represents the participating entity types will be foreign keys of R
	- any simple attribute of relationship in R

## Mapping EER Model Constructs to Relations

### Mapping of Specialization or Generalization

- Several options for mapping a number of subclasses that together form specialization (or generalization into superclass)
	- e.g.,: {SECRETARY, TECHNICIAN, ENGINEER}
- Two options: 
	- map the whole specialization into one single table
	- map it into multiple tables

#### Step 8: Options for Mapping Specialization or Generalization

convert each specialization with m subclass $\{S_1, S_2, ..S_m\}$ and superclass $C$ into one of the following

- **Option 8A: Multiple relations - superclass and subclass**
	- create a relation L for C with attributes $Attr(L) = \{k, a_1, a_2,..., a_n\}$, PrimaryKey $PK(L) = k$
	- create a relation $L_i$ for each subclass $S_i$ where $PK(L_i)=k$
	- primrary key of superclass C is propogated to $L_i$ and becomes its primray key
		- also becomes foreign key to superclass relation
		- an `EQUIJOIN` on the primary key between $L_i$ and $L$ produces all the specific and inherited attributes of entites in the $S_i$. 
	- This works for any specialization (disjoin or overlapping, total or partial)![[Screenshot 2024-05-25 at 4.05.51 PM.png]]
  
- **Option 8B: Multiple relations - subclass relations only**
	- Create a relation $L_i$ for each subclass $S_i, 1\leq i\leq m$, with attributes of 
		- $Attr(L_i) = \{Attr(S_i)\}\cup \{k, a_1, a_2, ...,a_m\}$ 
		- and $PK(L_i)=k$.
	- only works for a specialization whose subclasses are total 
	- recommended if specialization has disjointedness constraint 
	- `EQUIJOIN` operation between each subclass and superclass is built into the schema. 
	- No relation holds all the entites in superclass $C$, hence `OUTER JOIN` or `FULL OUTER JOIN` must be used. ![[Screenshot 2024-05-25 at 4.08.04 PM.png]]
- **Option 8C: Single relation with one type attribute**
	- Create a single relation $L$ with attributes 
		- $Attr(L) = \{k,a_1,.., a_n\} \cup \{Attr(S_i)\}. \cup ... \cup \{Attr(S_m)\} \cup t$
		and $PK(L)=k$, and t is type attribte to discremenate between different subclasses
		- ony fwork for specializatio where subclasses are disjoint 
	- may create many NULL values for subclass-specific attributes
	- Do not need `JOIN` operations 
- **Option 8D: Single relation with multiple type attributes**
	- Create a single relation $L$ with attributes 
		- $Attr(L) = \{k,a_1,.., a_n\} \cup \{Attr(S_i)\}. \cup ... \cup \{Attr(S_m)\} \cup \{t_1, t_2,..,t_m\}$
		and $PK(L)=k$, and $t_i$ is boolean type attribte to 
		- this when subclasses are overlapping but also works for disjoint classes
		- Do not need `JOIN` operations
- First two options are for multiple relations, last two for single relation 
- For multilevel specialization, multiple options can be used

### Mapping of Shared Subclasses (Multiple Inheritance)

- shared subclasses must all have the same key attribute, otherwise, use category (UNION) as discussed in [[Book Ch 4 - Enhanced Entity-Relationship (EER) Model]]. 
- Any of the options from 8 can be used

### Mapping of Categories (Union Types)

- A category (or union type) is a subclass of the union of two or more superclasses that can have different keys because can be different categories. 

#### Step 9: Mapping of Union Types (Categories) 

- create a surrogate key, a new key to unite all the superclasses. In the following, OWNER_id is the surrogate key
	- it is also recommended to add a type attribute in this
- For a category whose superclass has same key (e.g., Vehicle_id), no need to add a surrogate key
![[Screenshot 2024-05-25 at 4.28.03 PM.png]]