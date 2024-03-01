
/*
CREATE TABLE

--This SQL command is used to create a new table in the database
[AdventureWorks2022].[Sales].[Visit]-- This specifies the fully qualified name of the table. 
"AdventureWorks2022" is the database name, "Sales" is the schema name, and "Visit" is the table name.

visit_id INT PRIMARY KEY IDENTITY (1,1)--This defines the first column of the table named "visit_id" with the following properties
INT-- Specifies the data type of the column as integer.
PRIMARY KEY --Indicates that this column is the primary key for the table, ensuring uniqueness and 
providing a unique identifier for each row.
IDENTITY (1,1) -- Specifies that the column is an identity column, which automatically generates 
incremental values starting from 1 with a seed of 1 and an increment of 1 for each new row inserted into the table.

store_id INT NOT NULL--This line defines the store_id column with the following properties
INT--Specifies the data type of the column as integer.
NOT NULL--Specifies that this column cannot contain null values.
FOREIGN KEY (store_id) REFERENCES Sales.Storenew(store_id) 
This line creates a foreign key constraint on the store_id column, 
referencing the store_id column in the Sales.Storenew table. 
This ensures referential integrity by enforcing that the values in the store_id column of 
the Visit table must exist in the store_id column of the Sales.Storenew table.
*/

CREATE TABLE [AdventureWorks2022].[Sales].[Visit](
visit_id INT PRIMARY KEY IDENTITY (1,1),
first_name VARCHAR (50) NOT NULL,
last_name VARCHAR (50) NOT NULL,
visited_time  DATETIME,
phone VARCHAR(20),
store_id INT NOT NULL,
FOREIGN KEY (store_id) REFERENCES Sales.Storenew(store_id)
)

SELECT * From [AdventureWorks2022].[Sales].[Visit]


-----Temporary Tables----
--- are used to store intermediate results or temporary data during the execution 
--- of a specific session or a particular transaction. 

-----View-----
--- are virtual tables generated from a query result. They provide a way to present data stored in one or more 
--- tables in a structured format without actually storing the data physically. 


---Join---
---when we join two tables, we are linking them together via a selected characteristic.

SELECT column.names 
From table1.name1 join table.name2
ON column.name1 = column.name2

---Example---
--- AS- are used to assign aliases to the tables 
--- ON- used to specify the condition for joining tables in a JOIN operation.

SELECT * From [Person].[PhoneNumberType] AS e 
 join [Person].[PersonPhone] AS s
ON e.[PhoneNumberTypeID] = s.[PhoneNumberTypeID]

-----You can also specify the columns you want.

SELECT e.PhoneNumberTypeID, e.Name, s.PhoneNumberTypeID, s.PhoneNumber, s.BusinessEntityID From [Person].[PhoneNumberType] AS e 
 join [Person].[PersonPhone] AS s
ON e.[PhoneNumberTypeID] = s.[PhoneNumberTypeID] 

----Inner Join-----
--- Selects all rows from both the tables as long as the condition satisfies.

SELECT column.names From table1.name1 
inner join table.name2
ON column.name1 = column.name2

----Example----

SELECT * From [Person].[PhoneNumberType] AS e 
inner join [Person].[PersonPhone] AS s
ON e.[PhoneNumberTypeID] = s.[PhoneNumberTypeID] 

SELECT e.PhoneNumberTypeID, e.Name, s.PhoneNumberTypeID, s.PhoneNumber, s.BusinessEntityID From [Person].[PhoneNumberType] AS e 
inner join [Person].[PersonPhone] AS s
ON e.[PhoneNumberTypeID] = s.[PhoneNumberTypeID] 

------Right Join and Left Join----
---left  join - This join returns all the rows of the table on the left side of 
---the join and matching rows for the table on the rigth side of the join. And vice versa for the right join.

SELECT column.names From table1.name1 
left join table.name2
ON column.name1 = column.name2

----Examples---

----for right join--- 

SELECT * From [Person].[PhoneNumberType] AS e 
right join [Person].[PersonPhone] AS s
ON e.[PhoneNumberTypeID] = s.[PhoneNumberTypeID] 

SELECT e.PhoneNumberTypeID, e.Name, s.PhoneNumberTypeID, s.PhoneNumber, s.BusinessEntityID From [Person].[PhoneNumberType] AS e 
right join [Person].[PersonPhone] AS s
ON e.[PhoneNumberTypeID] = s.[PhoneNumberTypeID] 

----for left join--- 

SELECT * From [Person].[PhoneNumberType] AS e 
left join [Person].[PersonPhone] AS s
ON e.[PhoneNumberTypeID] = s.[PhoneNumberTypeID] 

SELECT e.PhoneNumberTypeID, e.Name, s.PhoneNumberTypeID, s.PhoneNumber, s.BusinessEntityID From [Person].[PhoneNumberType] AS e 
left join [Person].[PersonPhone] AS s
ON e.[PhoneNumberTypeID] = s.[PhoneNumberTypeID] 

