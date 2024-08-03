# Chapter 8 - The Relational Algebra and Relational Calculus

- Two formal languages for the relational model
	1. relational algebra
	2. relational calculus
- These were developed before SQL
- SQL primarily uses relational calculus with some ideas from relational algebra
- A data model must include
	- a set of operations to manipulate data
	- concepts for defining the database's structure and constraints 
- relational algebra is important 
	1. formal foundation for relational model operations
	2. basis for implementing and optimizing queries 
	3. part of SQL
- relational calculus provides a higher level declarative language for specifying relations queries 
	- no order of operations
	- important it has a firm math basis and is part of SQL
- Relational algebra operations groups 2
	1. set operations form set theory, applied because relations are set of tuples: UNION, INTERSECTION, SET DIFFERENCE, CARTESIAN PRODUCT (CROSS PRODUCT)
	2. operations developed for the relational database: SELECT, PROJECT, JOIN
	3. Aggregate functions: some requests can not be performed with original relational algebra, hence new operations: OUTER JOIN, OUTER UNIONs

## Unary Relational Operations: SELECT and PROJECT

- SELECT: Choose a subset based on a selection condition 
	- visualized as horizontal partitions into tuples that satisfy the condition and those that do not: $\sigma_{Dno=4}(EMPLOYEE)$

- The `SELECT` operation is as follows: $$\sigma_{<\text{selection} \quad \text{condition}>}(R)$$	 - $\sigma$ is SELECT operator
	 - `selection condition` is a boolean expression specified on the attributes of a relation $R$
	 - $R$ is relation
	 - The relation resulting from SELECT operator has the same attributes as $R$. 
 - **Selection condition** is a boolen expression made up of clauses
	 1. `<attribute name> <comparison op> <constant value>`
	 2. `<attribute name> <comparison op> <attribute name>`
	- comparison attribute $\in \{= <, \leq, >, \geq \neq \}$
	- constant value is constant value from attribue domain
	- clauses can be connected by `and, or, not`
	- **EXAMPLE:  $\sigma_{(Dno=40 AND Salary > 2500)}$
- all the comparison operators can be applied to attributes whos domains are ordered values 
	- (numeric, data)
	- strs are also ordered
- for unordered domain attributes, only $\{=, \neq\}$ can be used
- THe SELECT operaotr is applied as follows
	- selection condition applied independlelty on each individual tuple
	- if condition evaluates to TRUE -> t is selected
	- all selected tuples appear in the answer
- SELECTION operator is unary, 
	- applied to a single realtion.
	- applied to each tuple individualy
	- hence selection condition can not involve more than one tuple
- The degree of result (number of attributes) of SELECT is same as $R$
- The number of tuples of result $\leq$ tuples in $R$
	- $|\sigma_c(R)| \leq |\sigma(R)|$
- selection is commutative, hence a sequence of SELECT operators can be applied in any order

### Projection Operator

- chooses columns or attributes from given relation
	$\Phi_{<attribute \quad list>}(R)$
	
