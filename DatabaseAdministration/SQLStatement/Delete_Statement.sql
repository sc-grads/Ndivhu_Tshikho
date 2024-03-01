-----------------------------------------------------------------------------------
CREATE TABLE SalesStaff(
   staffid int NOT NULL PRIMARY KEY,
   fName nvarchar(50),
   lName nvarchar(50), 
   CountryRegion nvarchar(50) 
)

drop table SalesStaff

INSERT INTO SalesStaff 
SELECT BusinessEntityID,FirstName,LastName, CountryRegionNAme From Sales.vSalesPerson
SELECT * From SalesStaff

-----------------------------------------------------------------------------------

---DELETE - This keyword indicates that rows from a table should be deleted.
DELETE SalesStaff 
SELECT * From SalesStaff

DELETE From SalesStaff 
SELECT * From SalesStaff

-----------------------------------------------------------------------------------

DELETE From SalesStaff WHERE CountryRegion = 'United States'
SELECT * From SalesStaff

-----------------------------------------------------------------------------------

---BEGIN TRAN - This command begins a transaction, marking the start of a series of operations 
---that can be either committed or rolled back as a single unit.

Begin tran
DELETE From SalesStaff WHERE CountryRegion = 'United States'
----ROLLBACK TRAN - This command rolls back the changes made within the transaction
rollback tran

-----------------------------------------------------------------------------------

Begin tran
DELETE From SalesStaff WHERE CountryRegion = 'United States'
---COMMIT - This command commits the transaction. When a transaction is committed, 
---all changes made within the transaction are permanently saved to the database.
commit


SELECT * From SalesStaff

-----------------------------------------------------------------------------------
---SubQuery
--Is a query within another SQL query and embedded within there WHERE clause.

SELECT * FROM [HumanResources].[EmployeePayHistory]
--- WHERE clause filters the rows that are returned by the query.
WHERE BusinessEntityID IN (SELECT BusinessEntityID From [HumanResources].[EmployeePayHistory]  WHERE Rate > 60)

SELECT * From [Production].[Product] 
WHERE ProductID IN (SELECT ProductID From [Production].[ProductInventory] WHERE Quantity > 300)
DELETE SalesStaff

----------

WHERE staffid IN (SELECT BusinessEntityID From Sales.vSalesPerson WHERE SalesLastYear = 0)

SELECT * From SalesStaff

----OR----

DELETE SalesStaff
From Sales.vSalesPerson sp
INNER JOIN SalesStaff ss
ON sp.BusinessEntityID = ss.staffid WHERE sp.SalesLastYear = 0

SELECT * From SalesStaff

