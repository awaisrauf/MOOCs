# Design of Art Museum

## Specifications

Design a database to keep track of information for an art museum. Assume
that the following requirements were collected:
- The museum has a collection of ART_OBJECTS. Each ART_OBJECT has a unique Id_no, an Artist (if known), a Year (when it was created if known), a Title, and a Description. The art objects are categorized in several ways, as discussed below.
  
- ART_OBJECTS are categorized based on their type. There are three main types—PAINTING, SCULPTURE, and STATUE—plus another type called OTHER to accommodate objects that do not fall into one of the three main types.
  
- A PAINTING has a Paint_type (oil, watercolor, etc.), material on which it is Drawn_on (paper, canvas, wood, etc.), and Style (modern, abstract, etc.).
  
- A SCULPTURE or a statue has a Material from which it was created (wood, stone, etc.), Height, Weight, and Style.
- An art object in the OTHER category has a Type (print, photo, etc.) and Style.
  
- ART_OBJECTs are categorized as either PERMANENT_COLLECTION(objects that are owned by the museum) or BORROWED. Information captured about objects in the PERMANENT_COLLECTION includes Date_acquired, Status (on display, on loan, or stored), and Cost. Information captured about BORROWED objects includes the Collection from which it was borrowed, Date_borrowed, and Date_returned.
  
- Information describing the country or culture of Origin (Italian, Egyptian, American, Indian, and so forth) and Epoch (Renaissance, Modern, Ancient, and so forth) is captured for each ART_OBJECT.
  
- The museum keeps track of ARTIST information if known: Name, DateBorn (if known), Date_died (if not living), Country_of_origin, Epoch, Main_style, and Description. The Name is assumed to be unique.
  
- Different EXHIBITIONS occur, each having a Name, Start_date, and End_date. EXHIBITIONS are related to all the art objects that were on display during the exhibition.
  
- Information is kept on other COLLECTIONS with which the museum interacts; this information includes Name (unique), Type (museum, personal, etc.), Description, Address, Phone, and current Contact_person.

Draw an EER schema diagram for this application. Discuss any assumptions you make and then justify your EER design choices.

## EER Diagram 

[ExcelDraw Link for Better Visbility](https://excalidraw.com/#json=TN4D1Tb2-3GpmgiJ-1NqS,j5OhbunU8-JMBHIM-hGY5g)
![[Art_museum_EER.svg]]

## Justification

- `ART_OBJECT`'s Id_no is its key attribute
	- `Origin`: I created one simple attribute for the country or culture of origin as it should be just a name
	- `Epoch`: again a simple attribute 
	  
- `ART_OBJECT` has an N:1 relationship with `AUTHOR`. I assume that one object is created by only one author.
  
- `ART OBJECT` has an N: M relationship with `EXHIBITIONS` as N objects can be displayed for M exhibitions. 
  
- `PERMENANT_COLLECTION` and `BORROWED` are categories (union) of `ART_OBJECT` as it will only inherit properties of one of them. I am not sure of the total or partial nature of it
  
	- `BORROWED` has a 1:N relationship `BORROWED_FROM` with `EXTERNAL_COLLECTION` and this is a weak entity and identifying relationship as `Name` attribute is a partial key
	  
- `ART_OBJECT` has four disjoint subclasses 

### Feedback

It looks like most of the stuff in your EER is correct. 

1. ✅ I would look at how you treat identifying relationships for weak entities. Each identifying relationship should have double line connection with the weak entity which doesn’t seem the case in your picture. In most common case one leg of identifying relationship must be double line another may be either double or single. 

2. ✅We also usually have identifying relationships of one-to-many cardinality, the many-to-many identifying relationship is pretty suspicious. 

3. ✅ I would rather not treat Exhibition as a weak entity, we probably want to treat it as a strong entity, perhaps having as (name, start_date) as a composite identifier, as  instance of exhibition is actually mostly not dependent on particular instance of the art object. Even if some art object is not exhibited, but exhibition in general case would still exist without that object, so they are normally better represented as strong entity.

4. And yes, comparing with EER posted by Leo, it makes sense to have mandatory subclassing for ART_OBJECTS, we are probably covering all types in the subclasses especially have Other subclass.

5. I would think that your solution with having Union for Borrowed and Permanent  is acceptable as components have pretty different properties, but given that components are of the same nature, then maybe another subclassing like in Leo's picture will probably be more appropriate. But in case of Union each of the component must have its own identifier, otherwise, it would be a mistake, so you should take care oof this in your picture if you want to keep the Union.  In case of inheritance it would inherit Id_no and there will be no question of identifiers, so subclassing in this case as drawn in Leo's picture is after all probably better.  

6. The problem with the picture that Leo found however is that it does not show cardinalities, in all diagrams in this course you must show cardinalities of all relationships., otherwise you may lose points say in project Phase 1.  Also each entity must clearly show an identifier, unless it is a subclass or a weak entity (if weak, it should either have an identifying relationship and partial identifier, or in some cases more rarely two identifying relationships); I think your diagram follows this rule, though, it is just a general comment.

7. I also think Leo's diagram is more correct with respect to the Author who probably should not be considered as a weak entity as it can exist without ART-OBJECT and the Aname is meant to be a unique system-wide identifier.

# From EER to Relational Mapping

[ExcelDraw Link for a better view](https://excalidraw.com/#json=aCFIfCM6THMEvI62JP_Aw,3SQGspDYy0Cafe669xqMuQ)
![[relatoin_mapping.svg]]
### Justification
1. `ART_OBJECT`, `ARTIST`, `EXHIBITION`, and `EXTERNAL_COLLECTION` are converted into normal relations 
2. Relationship between `ART_OBJECT` and `ARTIST` is 1:N, hence, a Foreign key is inserted into `ART_OBJECT`
3. `EXHIBITION` and `ART_OBJECT` have N: M relationship, hence a new relation `EXHIBITED_AT` is introduced with two foreign keys connecting both relations 
4. Four disjoint subclasses of `ART_OBJECT` are converted into four new relations. All of them have `Id_no` as their primary and foreign key
5. Two disjoint subclasses of `ART_OBJECT` are converted into two relations with `Id_no` as their foreign and primary key
6. The `BORROWED` relation has an N:1 relationship with `EXTERNAL_COLLECTION`, hence primary key of `EXTERNAL_COLLECTION` is inserted into `BORROWED` as its foreign key

## SQL Schema

```SQL
CREATE SCHEMA 'Museum' AUTHORIZATION 'xyz';

-- main table --

CREATE TABLE ART_OBJECT (

PRIMARY KEY(Id_no),

Year NUMERIC(4),

Title CHAR VARYING(25) NOT NULL,

Description CLOB,

Origin CHAR VARYING(25),

Epoch CHAR VARYING(25),

FOREIGN KEY(ArtName) REFERENCES ARTIST

);

  

CREATE TABLE ARTIST(

PRIMARY KEY(ArtName),

DOB DATE,

DeathDate DATE,

Origin CHAR VARYING(25),

Epoch CHAR VARYING(25),

MainStyle CHAR VARYING(25)

);

  

CREATE TABLE EXHIBITION(

PRIMARY KEY(ExName),

StartDate DATE NOT NULL,

EndDate DATE NOT NULL,

);

  

CREATE TABLE EXHIBITED_AT(

FOREIGN KEY(Id_no) REFERENCES ART_OBJECT,

FOREIGN KEY(ExName) REFERENCES EXHIBITION

);

  

CREATE TABLE PAINTING(

FOREIGN KEY(Id_no) REFERENCES ART_OBJECT,

PaintType CHAR VARYING(25) NOT NULL,

DrawnOn CHAR VARYING(25) NOT NULL,

);

  

CREATE TABLE SCULPTURE(

FOREIGN KEY(Id_no) REFERENCES ART_OBJECT,

Material CHAR VARYING (25),

Height FLOAT(4,2) NOT NULL,

Width FLOAT(4,2) NOT NULL,

Style CHAR VARYING(25)

);

  

CREATE TABLE STATUE(

FOREIGN KEY(Id_no) REFERENCES ART_OBJECT,

);

  

CREATE TABLE OTHER(

FOREIGN KEY(Id_no) REFERENCES ART_OBJECT,

Type CHAR VARYING (25),

Style CHAR VARYING(25)

);

  

CREATE TABLE BORROWED(

FOREIGN KEY(Id_no) REFERENCES ART_OBJECT,

FOREIGN KEY(ColName) REFERENCES EXTERNAL_COLLECTION,

DateBorrowed DATE,

DateReturned DATE CHECK (DateReturned > DateBorrowed)

);

  

CREATE TABLE PERMENANT(

FOREIGN KEY(Id_no) REFERENCES ART_OBJECT,

DateAcquired DATE,

Status Boolean,

Cost FLOAT(7,2)

);

  

CREATE TABLE EXTERNAL_COLLECTION(

PRIMARY KEY (ColName),

Type CHAR VARYING (25),

Description CLOB,

Address CHAR VARYING (25),

Phone INT(10),

CurrentContactPerson CHAR VARYING (25)

  

);
```