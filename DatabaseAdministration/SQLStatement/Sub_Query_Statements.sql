Use AdventureWorks2022
GO

-----------------------------------------------------------------------------------
---SubQuery
--Is a query within another SQL query and embedded within there WHERE clause.

SELECT * FROM [HumanResources].[EmployeePayHistory]
--- WHERE clause filters the rows that are returned by the query.
WHERE BusinessEntityID IN (SELECT BusinessEntityID From [HumanResources].[EmployeePayHistory]  WHERE Rate > 60)

SELECT * From [Production].[Product] 
WHERE ProductID IN (SELECT ProductID From [Production].[ProductInventory] WHERE Quantity = 500)

