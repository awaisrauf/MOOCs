# Chapter 4 - Enhanced Entity-Relationship (EER) Model

## Subclasses, Superclasses and Inheritance

- **subclass or subtype of an entity**: when subgrouping is meaningful to represent explicitly 
- subclass (e.g., secretary) is the same as superclass (e.g, employee) with some distinct specific role
- we can represent members of the subclass as a distinct database object
- an entity can not exist by just being in a subclass, it must be in the superclass
- subclass inherits all the attributes of the superclass and all the relationships superclass participates

## Specialization and Generalization

### Specialization

- process of defining a set of subclasses of an entity type based on some distinguishing characteristics from superclass (e.g., EMPLOYEE to ENGINEER, TECHNICIAN)
- two reasons for subclasses
	- some subclasses may have attributes that others do not
	- some subclasses may participate in relations others do not
![[13.png]]

### Generalizatoin

- identifying common features of several entity types and generalize them into a single superclass

## Constraints and Characteristics of Specialization and Generalization Hierarchies

### Constraints on Specialization and Generalization

- for an entity to be a member of a certain subclass, there could be a condition  (defining predicate and predicate-defined) 
- membership condition could be based on attributes and will be called attribute-defined
- a subclass could also be based on the user, called a user-defined![[14.png]]
- Two constraints on specialization: 
	1. **disjointness or overlapping constraint**: subclasses must be disjoint sets, and the entity could be at most of one subclass
		- attribute-defined specialization implies disjointness constraint 
		- defined by d in the circle
		1. **overlapping**: if not disjoint. entity may be a member of more than one subclass of specialization ![[15.png]]
	1. **completeness or totalness constraint**: total or partial
		1. **total**: every entity in the superclass must be a member of at least one subclass, shown by double line ||. 
		2. **partial**: entity not to belong to any of the subclasses 
- These two constraints are independent and create 4 possibilities 
	- Disjoint, total 
	- Disjoint, partial
	- Overlapping, Total
	- Overlapping, partial 
  
### Specialization and Generalization Hierarchies and Lattices

- a subclass could further be a superclass, making a hierarchy or lattice of specialization 
	- **hierarchy**: if each subclass has only one parent
	- **lattice**: if some subclasses have more than one parent
  
## Modeling UNION Types using Categories

![[16.png]]
- to represent a collection of entities from different entity types (unions type or category)
	- it has two or more superclasses that may represent collections of entities from distinct entity types
	- whereas other sub/superclass relationships always have a single superclass
- In union, attribute inheritance works more selectively, OWNER entity interests attribute of one of the superclasses based on the ownership
- **total vs. partial category**: 
	- total category holds the union of all entities in the superclasses
	- partial category can hold a subset of the union 