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
