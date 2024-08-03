# Chapter 3 - Entity Relationship Model

- entity-relationship (ER) model

## Using High-Level Conceptual Data Models for Database Design

![[Book - Fundamentals of Database Systems/imgs/8.png]]

1. requirements collection and analysis: understand data requirements
	1. functional requirements: user-defined operations (transactions)
2. Conceptual Schema: description of data requirements of the users (entity types, relationship types, constraints)
3. implementation of database: SQL
4. physical design: internal file structure, indexes, access paths, etc.

## A Sample Database Application

- A COMPANY: keeps track of the company's
	- employees
	- departments
	- projects
- Mini-world description 
	- organized into departments each department has
		-  unique name
		- unique number
		- a particular employee of manages the department 
		- keep track of data employees began managing
		- may have several locations
	- A department controls several projects
		- unique name
		- unique number
		- single location
	- dataase stores employess
		- name
		- social security number
		- address
		- salary
		- gender
		- birth date
		- An employee is assigned to one department but may work on several projects, which may not be controlled by the same departments
		- required to keep track
			- of the number of hours per week that an employee works on each project
			- supervisor (who is another employee)
		- database will keep track of the dependents of each employee
			- first name
			- sex
			- Brith date
			- relationship to employee

## Entity Types, Entity Sets, Attributes, and Keys

![[Book - Fundamentals of Database Systems/imgs/9.png]]
- ER model describes databases as entities, relationships, and attributes
  
### Entities and Attributes

- **Entity**: a thing or object in the real world with independent existence
- **Composite vs Simple (atomic) Attribute**: ![[Book - Fundamentals of Database Systems/imgs/10.png]]
- **Single Valued vs. Multivalued Attributes**: 
- **Stored vs. Derived Attributes**: age can be derived from DOB
- **NULL Values**
- **Complex Attributes**: ![[11.png]]
  
### Entity Types, Entity Sets, Keys, and Value Sets

- an entity type defines a collection of entities that have the same attribute
	- e.g., 100 employees of a company
- entity set or entity collection: collection of all entities of a particular type at any point
- **Key Attributes of an Entity Type**
	- an entity type with no key is a weak entity type
	- no concept of the primary key
- **Value Sets (domains) of Attributes**: each entity type is associated with a value set (domain value)
  
## Relationship Types, Relationship Sets, Roles, and Structural Constraints

- many implicit relationships among entity types
	- whenever an attribute of one entity type refers to another entity type, some relationship exists

## Relationship Types, Sets, and Instances

- A relationship type $R$ among $n$ entities $E_1, E_2,..,E_n$ defines a set of associations or relationships. 
- Each entity type is said to participate in the relations type R

### Relationship Degree, Role Names, and Recursive Relationships

- **Degree**: number of participating entity types
	- most common are binary relationships

#### Participation Constraints

- defines whether the existence of an entity depends on its being related to another entity via relationship type
	- minimum cardinality constraint: minimum number of relationship instances that each entity can participate 
- **total and partial**:
	- if an employee can not exist if they are not connected with a department, this is total participation (also an existence dependency)
	- if an employee may manage a department, it's a partial management
- total participation with double-line
- partial participation single-line

#### Attributes of Relationship Types

- 1:1 and 1:N relationship types can be migrated to one of the participating entity types

## Weak Entity Types

- Entity types without key attribute
	- other entities the weak entities are related to are called the **owner or identifying entity type**
	- a weak entity type always has a total participation constraint (existence dependency) because weak entities can not be identified without an owner
	- weak entity normally has a partial key 