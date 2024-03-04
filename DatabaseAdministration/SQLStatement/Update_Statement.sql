use AdventureWorks2022
GO


SELECT 
FirstName+ ' ' + LastName AS FullName,
TerritoryName,
TerritoryGroup,
SalesQuota,
SalesYTD,
SalesLastYear
INTO salesstaff
From Sales.vSalesPerson

---SELECT INTO - operation, retrieves data from one table and inserts it into a new table.
---From - This specifies the source table from which data will be retrieved.

------------------------------------------------------------------------------------
---This is the command used to delete a table from the database
drop table salesstaff;

------------------------------------------------------------------------------------
--
---UPDATE - This keyword is used to indicate that data within a table will be modified.
---SET - This keyword is used to specify which column(s) will be modified and what their new values will be.

UPDATE SalesStaff SET salesquota = 500000.00
SELECT * From salesstaff

UPDATE SalesStaff SET salesquota = salesquota + 150000.00 
SELECT * From salesstaff

UPDATE SalesStaff SET salesquota = salesquota + 150000.00,SalesYTD = SalesYTD - 50, SalesLastYear = SalesLastYear *1.50
SELECT * From salesstaff

------------------------------------------------------------------------------------

UPDATE SalesStaff SET TerritoryName = 'UK' WHERE TerritoryName = 'United Kingdom'
SELECT * From salesstaff

UPDATE SalesStaff SET TerritoryName = 'UK' WHERE TerritoryGroup is NULL and FullName = 'Syed Abbas'
SELECT * From salesstaff

------------------------------------------------------------------------------------
/*
UPDATE SalesStaff SET salesquota = sp.salesquota
From SalesStaff ss
Inner join sales.vSalesPerson sp
ON ss.FullName = sp.FirstName +' '+ sp.LastName

SELECT * From salesstaff