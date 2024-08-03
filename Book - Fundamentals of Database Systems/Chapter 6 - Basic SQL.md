# Book Ch 6 - Basic SQL

- SQL being standard helped its popularity 
- Relational algebra is too low-level for most commercial DMBS and difficult for users since in it query has to be written as a sequence of operations that when executed, produce the results
- SQL provides a higher-level declarative language interface. 
  
## SQL Data Definition and Data Types

- table, row, and column for relation, tuple, and attribute 
- The main command `CREATE`, a statement that is used for 
	- schemas
	- tables (relations)
	- types
	- domains
	- constructs (such as views, assertions, triggers)

### Schema and Catalog Concepts in SQL

- SQL schema is identified by a schema name and authorization identifier (who owns the schema), a descriptor for each element
- Schema element include 
	- tables, types, constraints, views, domains, and other constructs 
- To create a schema, use the CREATE statement
```SQL
CREATE SCHEMA COMPANY AUTHORIZATION 'Jsmith';
```

- **Catalog**: a named collection of schemas
	- always contains a special schema called INFORMATION_SCHEMA provides info about all the schemas, element descriptors in the schemas 
	- Integrity constraints can only be applied if relations exist within the same catalog

### Create Table Command in SQL

- `CREATE TABLE` is used to specify a new relation by giving its name, specifying attributes, and possible initial constraints.
  
- `ALTER TABLE` can also be used to change parts of the table
  
- SCHEMA name can be specified in the environment or explicitly in the CREATE TABLE command 
	  `CREATE TABLE COMPANY.EMPLOYEE`
	rather than
	 `CREATE TABLE EMPLOYEE`
 ![[Book - Fundamentals of Database Systems/imgs/3.png]]
 -  **base tables**: Relations created by `CREATE TABLE` are called base tables
	 - as the table and its rows are actually created by DBMS
 - **Virtual Table: Created by the `CREATE VIEW` command
 - In SQL: 
	 - attributes in the base table are ordered in the sequence of their input, 
	 - rows (tuples) are not ordered within a table
 - Some foreign key constraints may not work initially as there are no tables correspondingly. SO use ALTER TABLE afterwards

### Attribute Data Types and Domains in SQL

The basic data types available for attributes are numeric, char, str, bit str, boolean, date, and time

- **Numeric**: INT, SMALL INT, FLOAT, REAL, DOUBLE PRECISION. 
	- Formatting `DECIMAL(i, j)` or `DEC(i, j)` or `NUMERIC(i, j)` where $i$ is: the total number of decimal digits and $j$ (scale) is the number of digits after decimal points
	- the default scale is 0
- **Character-string**: 
	- either fixed length `CHAR(n)`, `CHARACTER(n)` where n is number of characters
	- varying length `CHAR VARYING(n)` where n is maximum chars 
	- placed between single quote marks and case-sensitive
	- comparison: str are ordered in alphabetic
	- concatentaiton: `||` : 'abc' || 'XYZ' = 'abcXYZ'
	- `CLOB` or `CHARACTER LARGE OBJECT` for larger text whose length is defined in kilo, mega or gigabytes (e.g., `CLOB(20M)`)
- **Bit-string**: 
	- fixed lenght `BIT(n)`
	- or vayring `BIT VARYING(n)` n is max number of bits
	- example: `B'10010'` 
	- `BLOB` or `BINARY LARGE OBJECT` for columns with large binary values, e.g, `BLOB(30M)`
- **Boolean**: Three valued logic: TRUE, FALSE or UNKNOWN (for NULLs)
- **Time-related**
	- **DATE**: 
		- DATE: ten positions with YEAR, MONTH,DAY (`YYYY-MM-DD`)
		- TIME: at least 8 digits (HOUR, MINUTE, SECOND) `HH:MM:SS`
		- single-quoted strings preceded by the keyword DATE or TIMEEXAMPLE: `DATE: '2014-09-27`
		- `TIME(i)`: where `i` is time fractional seconds precision, specifies `i+1` additional positions for TIME
			- 1 position for an additional period (.) as separator char
			- i position for decimal fractions of a second
		- TIME WITH TIME ZONE data type includes an additional six positions for specifying displacement from Standard time zone in HOURS: MINUTES
		- The default timezone is the local SQL session's timezone
	- **TIMESTAMP**: 
		- example: TIMESTAMP ‘2014-09-27 09:12:47.648302
	- **INTERVAL** is a relative value to increment or decrement the absolute value of a date or time in the format of YEAR/MONTH or DAY/TIMe
	- all these can be considered as special type of string
- It is possible to use specific new data types
	```SQL
	CREATE DOMAIN SSN_TYPE AS CHAR(9);
```
## Specifying Constraints in SQL

### Specifying Attribute Constraints and Attribute Defaults

- NO NULL to not allow NULL values, default for primary key attributes
- possible to specify `default value` by `DEFAULT <value>` in attribute definition, for most attributes NULL is the default DEFAULT
- **CHECK**: restrict attribute values. EXAMPLE: The Dnumber should be between 1 and 20. 
	```SQL
	Dnumber INT NOT NULL CHECK (Dnumber > 0 AND Dnumber <21)
```
	 - Can also be used with CREATE DOMAIN statement 
		```SQL
		CREATE DOMAIN D_NUM AS INTEGER 
		 CHECK (D_NUM > 0 AND D_NUM < 21)
``` 
	- now D_NUM domain type can be used for all attributes that define this
### Specifying Key and Referential Integrity Constraints 
- **Key Constraint**: Special clause 'PRIMARY KEY' in CREATE TABLE to specify one or more attributes as PRIMARY KEY
	```SQL 
	Dnumber INT PRIMARY KEY
```
- The `UNIQUE` clause specifies alternate (unique) keys (candidate keys). It can also specified as a unique key for a single attribute
	```SQL
	Dname VARCHAR(15) UNIQUE
```
- **Referential Integrity** is forced via the `FOREIGN KEY` clause 
	- can be violated when
		- a tuple is inserted or deleted
		- foreign key or primary key attribute is updated
	- **on integrity violation**,
		- default action is reject (RESTRICT) 
		- schema can define alternative  by attaching a referential triggered action clause to any foreign key constraint, options include
			1. SET NULL
			2. CASCADE: 
			3. SET DEFAULT
		- Operations must be qualified: ON DELETE SET NULL or ON UPDATE CASCADE
	- CASCADE: The action for
		-  CASCADE ON DELETE is to delete all the referencing tuples
		- CASCADE ON UPDATE is to change the value of the referencing foreign key attributes to primary key values for all the referencing tuples
![[Screenshot 2024-05-22 at 6.11.46 PM.png]]
### Giving Names to Constraints
- possible to give name constraints but they must be unique
### Specifying Constraints on Tuples Using Check

- additional constraints can be applied with CHECK at the end of CREATE TABLE
	- constraints work row-wise as they applied on individual rows
	```SQL
	CHECK(Dept_create_date <= Mgr_start_date);
```


## Basic Retrieval Queries in SQL

- One basic statement for retrieving info from the database: `SELECT`
	- it's not the same as SELECT from relational algebra
- A difference between the practical SQL model and the formal relational model
	- SQL allows a table to have two or more tuples that are identical in all attributes
	- Hence, an SQL table is not a set of tuples but a multiset or bag of tuples
- Some SQL relations can be set because of KEY constraint or DISTINCT option
  
### The SELECT-FROM-WHERE Structure of Basic SQL Queries

- A basic form of SELECT statement (also called mapping or select-from-where block) is
	1. **SELECT** `<attribute list>`
	2. **FROM** `<table list`
	3. **WHERE** `<condition>`;
- Basic comparison operators for comparing attribute values with one another and literal constants are
	- `=, <,>, <=, >=` and `<>`(not equal)
- **EXAMPLE**: retrieve the name and address of all the employees who work for the Research dept
```SQL
SELECT Fname, Lname, Address
FROM   EMPLOYEE, DEPARTMENT
WHERE  Dname='Research' AND Dnumber= Dno;
```

-  The `Dnumber=Dno` is called a joint condition as it combines two tuples: one from DEPARTMENT and one from EMPLOYEE whenever the value of Dnumber in DEPARTMENT is equal to the value of Dno in EMPLOYEE. 

- A query that involves only selection and join conditions plus projection is called a **select-project-join** query
- **EXAMPLE**:

```SQL
	SELECT Pnumber, Dnum, Lname, Address, Bdate
	FROM PROJECT, DEPARTMENT, EMPLOYEE
	WHERE Dnum = Dnumber AND Mgr_ssn=Ssn AND Plocation = 'Stafford'
```

### Ambiguous Attribute Names, Aliasing, Renaming, and Tuple Variables

- **Name Ambiguity**: SQL, the same name can be used for two attributes as long as they are in different tables.
	- to prevent such confusion, one must qualify the attribute name with the relation name
	```SQL
	SELECT Fname, EMPLOYEE.Name, Address
	FROM   EMPLOYEE, DEPARTMENT
	WHERE  DEPARTMENT.Dnumber=EMPLOYEE.Dnumber
```

- Fully qualified attributes can also be used even when no ambiguity 
- Aliases of names can also be created to shorten them. we are also required to declare `aliases` or `tuple variables`. by either using `AS` in `FROM` or by using the following which also aliases attributees within the query 

```SQL
	EMPLOYEE AS E(Fn, Mi, Ln, Ssn, Bd, Addr, Sex, Sal, Ssssn, Dno)
```

- **SAME Attribute Twice**

```SQL
SELECT E.Fname, E.Lname, S.Fname, S.Lname
FROM EMPLOYEE AS E, EMPLOYEE AS S
WHERE E.Super_ssn = S.Sssn
```

- this is one level of recursive query

### Unspecified WHERE Clause and Use of the Asterisk

- if no WHERE is specified, all attributes are selected from the relation
- if no `WHERE` is specified with two relations in `FROM`, all cross-products are selected
	- it is important to specify every selection and join condition in `WHERE`, otherwise very large relations may result. 
- To retrieve all the attribute values, use the asterisk `*`

```SQL
	SELECT *
	FROM EMPLOYEE
	WHERE Dno=5;
```

	- it can also prefix relation names or aliases: `EMPLOYEE.*` means all attributes of EMPLOYEE

### Tables as Sets in SQL

- In SQL, tables are not sets, rather multisets and duplicate tuples may appear
- An SQL table with a Key is restricted to being set since the key needs to be unique
- Can use `DISTINCT` in `SELECT` to remove duplicates in the resulting relation
- `ALL` can also be used to get all results which is also the default

```SQL
SELECT ALL Salary
FROM EMPLOYEE
```

```SQL
SELECT DISTINCT Salary
FROM EMPLOYEE;
```

- SQL has some operations directly from set theory. The result of these operations are sets (duplicates removed)
	- `UNION`
	- Set difference (`EXCEPT`)
	- intersection `INTERSECT`
- These can only be applied to compatible relations: both relations must have the same attributes in the same order

```SQL
(SELECT DISTINCT Pnumber
FROM PROJECT, DEPARTMENT, EMPLOYEE
WHERE Dnum=Dnumber AND Mgr_ssn = Ssn
	  AND Lname='Smith')
UNION
(SELECT DISTINCT Pnumber
 FROM PROJECT, WORKS_ON, EMPLOYEE
 WHERE Pnumber=Pno AND Essn=Ssn
	 AND Lname = 'Smith'
)
```

- Can also have these operations with `ALL` but in this case results will not be set. 

### Substring Pattern Matching and Arithmetic Operations

- `LIKE` comparison operator to compare parts of a character string
	- partial strings are specified using two reserved chars 
		- `%`: replaces an arbitrary number of zero or more chars
		- underscore `_` replaces a single character 

```SQL
	SELECT Fname, Lname
	FROM EMPLOYEE 
	WHERE Address LIKE '%Houston,TX%'
```

- Find all employees who were born during the 1950s
 ```SQL
 SELECT Fname, Lname
 FROM EMPLOYEE
 WHERE Bdate LIKE '_ _ 7 _ _ _ _ _ _ _'
```
- if a literal `%` is required, it should be preceded by `\` such as `AB_CD\%EF`
----
**Arithmetic Operations**
	- standard arithmetic operations can be applied, for instance, giving a 10% raise to employees on a certain project will be 
**EXAMPLE**: Show the result of salaries if every employee working on the ProductX project is given a 10% raise

```SQL
SELECT E.Fname, E.Lname, 1.1*E.Saraly AS Increased_sal
	FROM EMPLOYEE AS E, WORKS_ON AS W, PROJECT AS P
	WHERE E.Ssn = W.ESsn AND W.Pno = P.Pnumber AND P.Name = 'ProductX'
```
- For string types, the concatenate operator `||` can be used in a query to append two string values. 
- For data, time, and similar data types, `+`, `-` can be used for interval increment 
- `BETWEEN`
	**EXAMPLE**: Retrieve all employees in department 5 whose salary is between $30000 and $40000
	```SQL 
	SELECT *
	FROM EMPLOYEE
	WHERE (Salary BETWEEN 30000 AND 40000) AND Dno=5;
```
### Ordering of Query Results 
- `ORDER BY`SQL allows result tuples to be ordered by the value of one or more attributes that appear in the query result 
	- **EXAMPLE**: Retrieve a list of employees and projects they are working on ordered by department and within each department, ordered alphabetically last name, first name
```SQL
SELECT D.Dname, E.Lname, E.Fname, P.Pname
FROM DEPARTMENT AS D, EMPLOYEE AS E, WORKS_ON W, PROJECT AS P
WHERE D.Dnumber = E.Dno AND E.Ssn = W.ESsn AND W.Pno = P.Pnumber
ORDER BY D.Dname, E.Lname, E.Fname ASC
```
- The default order is DESC but ASC can be specified by ASC keyword

## INSERT, DELETE, and UPDATE Statements in SQL

- three commands to modify datasets 
	- `INSERT`
	- `DELETE`
	- `UPDATE`
  
### The `INSERT` Command

- `INSERT` is used to add a single tuple (row) in the table (relation)
	- must add-relation name and list of values for the attributes
	- order or original table should be followed
	```SQL
	INSERT INTO EMPLOYEE 
	VALUES ('Richard', .......)
```
- A second form can allow users to specify attributes
	- but must include all attributes with NO NULL restriction and no default options
```SQL 
INSERT INTO EMPLOYEE(Fname, Lname, Dno, Ssn)
VALUES ('Name)
```

- Adding multiple tuples is also possible 
- Two more forms: 1) inserting during CREATE Table and creating a table from results of SELECT![[Book - Fundamentals of Database Systems/imgs/5.png]]
	- `WORKS_ON_INFO` is created and be searched and worked on 
	- DELETE by using the `DROP TABLE` command 
	- This table will not be updated with updates in the WORKS_ON table. For that, view creation is necessary 
- To create a like one already exists, `LIKE` command is used 
```SQL
	CREATE TABLE D5EMPS LIKE EMPLOYEE
	(SELECT E.*
	FROM EMPLOYEE AS E
	WHERE E.Dno=5) WITH DATA;
```
	- `WITH DATA` will preload the table with the data

### The DELETE Command
- removes tuples from relation and includes `WHERE` clause to select tuples to be deleted
- deleted from only one table but deletion can propagate if referential triggered actions are specified 
- 0, 1, or several tuples from one table can be deleted 
- Deleting all the data from the table does not delete tables, it remains empty which can be removed by `DROP BY`
```SQL
DELETE FROM EMPLOYEE
WHERE Lname='Brown';
```

### The Update Command

- used to modify attribute values of one or more selected tuples
	- `WHERE` clause selects tuples to be modified from a single relation
	- updating the primary key may propagate to may propagate it to foreign keys if such action is specified 
	- `SET` clause specifies attributes to be modified and their value
	**EXAMPLE**
	```SQL
	UPDATE PROJECT
	SET Plocation = 'Bellaire', Dnum=5
	WHERE Pnumber=10;
```
- Several tuples can be set with a single command 
```SQL 
UPDATE EMPLOYEE
SET Salary=Salary*1.10
WHERE Dno=5
```