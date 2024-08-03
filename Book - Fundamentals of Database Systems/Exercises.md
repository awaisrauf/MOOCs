# Exercises

----
**Question:** Figure 9.8 shows an ER schema for a database that can be used to keep track of
transport ships and their locations for maritime authorities. Map this schema
into a relational schema and specify all primary keys and foreign keys. ![[20.png]]
**Answer**:
SHIP_TYPE(**Type**,Toognage, Hull, *FK{**Ship_name**, SHIP}*)
STATE_COUNTRY(**Name**, Continent)
WATER_BODY(**Name**)
SHIP(**Sname**, Owner, *FK{**Port_name**, PORT}*, *FK{**Ship_type**, SHIP_TYPE}*)
SHIP_MOVEMENT(*FK{**Ship_name**, SHIP}*, **Date**, **Time**, Longitude, Latitude)
PORT(**Pname**, **State_name**, **Water_body_name**,*FK{**State_name**, STATE_NAME}*, *FK{**Sea_name**}, WATER_BODY* )
PORT_VISIT(**Start_date**, End_date, **Ship_name**, **Port_name**)
SHIP_AT_PORT(Port_name, Ship_name)

----

![[21.png]]

---
**Question:** Specify the following queries in SQL on the database schema of Figure 1.2. 
1. Retrieve the names of all senior students majoring in ‘cs’ (computer science). 
2. b. Retrieve the names of all courses taught by Professor King in 2007 and 2008. 
3. c. For each section taught by Professor King, retrieve the course number, semester, year, and number of students who took the section. 
4. d. Retrieve the name and transcript of each senior student (Class = 4) majoring in CS. A transcript includes the course name, course number, credit hours, semester, year, and grade for each course completed by the student.![[Screenshot 2024-06-23 at 7.18.45 PM.png]]
**Answer**
1. a
```SQL
SELECT Name
FROM STUDENT
WHERE Class='Senior' AND Major='cs'
```
2. 
```SQL
SELECT C.Course_name
FROM SECTION AS S, COURSE AS C
WHERE S.Course_number=C.Course_number AND S.Instructor='King' AND (S.Year= 2007 OR S.Year=2008)

```
3. s
```SQL
SELECT Course_number, Semester, Year, Count(*)
FROM SECTION AS S, GRADE_REPORT AS GR
WHERE S.Section_identifier=GR.Section_identifier AND S.Instructor='King'
GROUP BY S.Section_identifier
```

4. s
```SQL
SELECT Course_name, Course_number, Credit_hours, Semester, Year, Grade
FROM SECTION AS S, COURSE AS C, GRADE_REPORT AS GR, STUDENT AS ST
WHERE S.Course_number=C.Course_number AND S.Section_identifier=GR.Section_identifier AND GR.Student_number=ST.Student_number AND ST.Class=4
```

---
**Question:** In SQL, specify the following queries on the database in Figure 5.5 using the concept of nested queries and other concepts described in this chapter.

1. Retrieve the names of all employees who work in the department that has the employee with the highest salary among all employees.
2. Retrieve the names of all employees whose supervisor’s supervisor has ‘888665555’ for Ssn.
3. Retrieve the names of employees who make at least $10,000 more than the employee who is paid the least in the company.
![[22.png]]
**Answer**: 
1. Retrieve the names of all employees who work in the department that has the employee with the highest salary among all employees.

```SQL
SELECT Fname, Lname
FROM EMPLOYEE
WHERE Dno IN (SELECT Dno
			  FROM EMPLOYEE 
			  WHERE Salary = (SELECT Max(Salary)
							  FROM EMPLOYEE))
```

2. Retrieve the names of all employees whose supervisor’s supervisor has ‘888665555’ for Ssn.
```SQL
SELECT Fname, Lname
FROM EMPLOYEE as e 
	JOIN EMPLOYEE AS sueprvisor ON supervisor.Ssn=Ssn
	JOIN supervisor_supervisor ON supervisor_supervisor.Ssn=supervisor.Ssn
WHERE supervisor_supervisor.Ss=888665555
```

3. Retrieve the names of employees who make at least $10,000 more than the employee who is paid the least in the company.
```SQL
SELECT Fname, Lname
FROM EMPLOYEE
WHERE Salary >= (SELECT MIN(Salary)
				FROM EMPLOYEE) + 10000

```

---- 
