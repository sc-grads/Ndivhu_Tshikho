use AdventureWorks2022
go
--Join
--Is used to combine rows from two or more tables, based on a related column between them.
--Join Condition 

-- defines the way two tables are related in aquery by:

-- 1. Specifying the column from each table to be used for the join.
-- It specifies the foreign key from one table and it's associated key in the other table.

-- 2. Specifying a logical operator for example ( =, or, <>) to be used in comparing values from the column.

---Snytax
/*
SELECT column.names
From table1.name1 join table2.name2
ON column.name1 = column.name2
condition
*/

SELECT* From [Sales].[Customer];

SELECT* From  [Sales].[SalesOrderHeader] 
---Joining customer(sales) and SaleOrderHeader (sales)
SELECT sc.CustomerID,sc.PersonID, sc.StoreID, ss.SalesOrderID, ss.OrderDate, ss.BillToAddressID From [Sales].[Customer] sc  join [Sales].[SalesOrderHeader] ss
ON sc.CustomerID = ss.CustomerID 


SELECT ss.CustomerID, ss.SalesOrderID, sc.PersonID, sc.StoreID, sc.TerritoryID, ss.CreditCardID, ss.BillToAddressID 
From [Sales].[Customer] sc   join [Sales].[SalesOrderHeader] ss
ON sc.CustomerID = ss.CustomerID -- WHERE ss.CustomerID LIKE '%28168'

--Inner join
--Select all rows from both the tables as long as the condition satisfies.
--In an INNER JOIN, only rows with matching values in both tables are included in the result set. Unmatched rows are excluded.

SELECT* From [Sales].[Customer] sc  inner join [Sales].[SalesOrderHeader] ss
ON sc.CustomerID = ss.CustomerID

--Right join
--This returns all the rows of the table on the right side of the join and 
--matching rows for the table on the left side.
--In a RIGHT JOIN, all rows from the right table are included in the result set,
--and unmatched rows from the left table  are represented with NULL values for the columns from the left table.

SELECT* From [Sales].[Customer] sc  right join [Sales].[SalesOrderHeader] ss
ON sc.CustomerID = ss.CustomerID

--left join
--This returns all the rows of the table on the left side of the join and 
--matching rows for the table on the right side.
--In a LEFT JOIN, all rows from the left table  are included in the result set, 
--and unmatched rows from the right table are represented with NULL values for the columns from the right table.

SELECT* From [Sales].[Customer] sc  left join [Sales].[SalesOrderHeader] ss
ON sc.CustomerID = ss.CustomerID

--Full Join
--Creates the result set by combining results of both the left and right join.
--Result-set will contain all the rows from both the tables.
--The rows at which the is no matching, the result-set will contain NULL values.

SELECT* From [Sales].[Customer] sc  full join [Sales].[SalesOrderHeader] ss
ON sc.CustomerID = ss.CustomerID


---Example from the udemy course---

CREATE TABLE Employee(
    EmpID int PRIMARY KEY,
	EmpName nvarchar(50) NULL,
	EmpTitle nvarchar(50) NULL,
)
 drop table Employee
INSERT INTO Employee (EmpID, EmpName, EmpTitle) values (3, 'Dino', 'Sales Associate'),(79, 'James', 'Sales Manager'), (11, 'Issa', 'Sales Associate'),  (39, 'Bihaag', 'Sales Executive')

SELECT * From Employee;


CREATE TABLE Sales(
EmpName varchar(50) NULL,
SaleNumber int  NOT NULL,
ItemSold int NULL,
EmpID INT NULL,
FOREIGN KEY (EmpID) REFERENCES Employee (EmpID)
)

drop table Sales
SELECT * From Employee;
SELECT * From Sales;

INSERT INTO Sales (EmpName, SaleNumber,ItemSold, EmpID) values ('Dino', 23, 44, 3),('Dino', 125, 11, 3),('Issa', 8798, 11, 11), 
('Issa', 258, 44, 11),('Issa', 14, 56, 11), ('Dino', 8989, 123, 3)


SELECT * From Employee e Inner Join sales s
ON e.EmpID = s.EmpID 

SELECT * From Employee e Full Join sales s
ON e.EmpID = s.EmpID 

SELECT * From Employee e Right Join sales s
ON e.EmpID = s.EmpID 

SELECT * From Employee e Left Join sales s
ON e.EmpID = s.EmpID 


