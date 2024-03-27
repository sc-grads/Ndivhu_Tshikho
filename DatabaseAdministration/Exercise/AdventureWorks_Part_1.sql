USE AdventureWorks2022
GO

-- 1.
Select * from [HumanResources].[Employee]
order by [JobTitle] ASC


-- 2.
Select [BusinessEntityID], [PersonType],[NameStyle], [Title] ,[FirstName]  from [Person].[Person]
order by [LastName] ASC

-- 3.
Select [FirstName],[LastName], [BusinessEntityID] AS Employee_ID from [Person].[Person]
Order By [LastName]

-- 4.
Select [ProductID], [ProductNumber], [Name]   
From [Production].[Product]
Where [SellStartDate] is not null and [ProductLine] like 'T%'
Order By [Name]

-- 5.
--Not Accurate 
Select [SalesOrderID], [CustomerID], [OrderDate], [SubTotal],
       [TaxAmt] * 100 AS Tax_Percent 
from [Sales].[SalesOrderHeader]
Order By  [SubTotal] ASC

-- 6.
Select Distinct JobTitle From [HumanResources].[Employee]

-- 7. 
Select [CustomerID],sum([Freight]) as Total_Freight  
From  [Sales].[SalesOrderHeader]
Group By [CustomerID] 
Order By [CustomerID] ASC

-- 8. 
Select [CustomerID], [SalesPersonID],avg([SubTotal]) as Avg_SubTotal,
       sum([SubTotal]) as Sum_SubTotal
from [Sales].[SalesOrderHeader]
Group By [CustomerID], [SalesPersonID]
Order By [CustomerID] DESC


-- 9.
 Select [ProductID], sum([Quantity]) as Total_Quantity 
 from [Production].[ProductInventory]
 WHERE [Shelf] = 'A' or  [Shelf] = 'C' or [Shelf] = 'H'
 Group By [ProductID]

-- 10.

-- 11.
Select P.[BusinessEntityID], P.[FirstName], P.[LastName], PP.[PhoneNumber] 
from [Person].[Person] As P
Join
 [Person].[PersonPhone] As PP
ON P.BusinessEntityID = PP.BusinessEntityID
Where P.[LastName] Like 'L%'
Order By P.[LastName] , P.[FirstName]

-- 12.


-- 13. 

Select [LocationID],[Shelf],  sum([Quantity] ) as TotalQuantity from [Production].[ProductInventory]
Group By[LocationID], [Shelf]
Order By [LocationID]

-- 14.

