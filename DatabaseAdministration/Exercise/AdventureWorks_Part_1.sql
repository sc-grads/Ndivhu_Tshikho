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

Select sum([Quantity]) As [Total Quantity] from [Production].[ProductInventory]
Group By [LocationID]
Order By [LocationID] * 10


-- 11.
Select P.[BusinessEntityID], P.[FirstName], P.[LastName], PP.[PhoneNumber] 
from [Person].[Person] As P
Join
 [Person].[PersonPhone] As PP
ON P.BusinessEntityID = PP.BusinessEntityID
Where P.[LastName] Like 'L%'
Order By P.[LastName] , P.[FirstName]

-- 12.
-- Not Accurate 
Select [SalesPersonID],[CustomerID], sum([SubTotal]) as [Sum SubTotal] from [Sales].[SalesOrderHeader]          
Group By [SalesPersonID],[CustomerID]
Select * from [Sales].[SalesOrderHeader]
-- 13. 
 
Select [LocationID],[Shelf], sum([Quantity] ) as TotalQuantity from [Production].[ProductInventory]
Group By[LocationID], [Shelf]

-- 14.
-- Not Accurate 
select [LocationID],[Shelf], sum([Quantity] ) as TotalQuantity from [Production].[ProductInventory]
Group By Rollup([LocationID],[Shelf])

-- 15. 

Select [LocationID],  sum([Quantity] ) as TotalQuantity from [Production].[ProductInventory]
Group By[LocationID]

-- 16. 

Select (PA.City) as city, count(BEA.BusinessEntityID) as noofemployees 
from [Person].[Address] As PA
Join [Person].[BusinessEntityAddress] as BEA
ON PA.AddressID = BEA.AddressID
Group By PA.City 
Order By PA.City ASC

-- 17.
Select  Year([OrderDate]) as Year,sum([TotalDue]) as [Order Amount]  from [Sales].[SalesOrderHeader]
Group By Year([OrderDate])
Order By Year([OrderDate])

-- 18.
Select  Year([OrderDate]) as YearForOrderDate,sum([TotalDue]) as [OrderDueAmount]  from [Sales].[SalesOrderHeader]
Where OrderDate <= '2016' 
Group By Year([OrderDate])
Order By Year([OrderDate]) ASC

-- 19.
Select[ContactTypeID], [Name]  from [Person].[ContactType]
Where [Name]  Like '%Manager' 
Order By [Name]  DESC

-- 20. 
Select BEC.BusinessEntityID, PP.LastName, PP.FirstName from [Person].[BusinessEntityContact] as BEC
 join  [Person].[Person] as PP
ON BEC.BusinessEntityID = PP.BusinessEntityID
--Order By PP.LastName, PP.FirstName ASC

-- 21.
-- Not accurate 
select SP.SalesYTD, [PostalCode] From [Sales].[SalesPerson] as SP
Inner Join [Person].[BusinessEntityAddress] As PB
ON SP.BusinessEntityID = PB.BusinessEntityID
Inner Join [Person].[Address] AS PA
ON PB.AddressID = PA.AddressID
WHERE SP.SalesYTD != 0
Group By SP.SalesYTD, [PostalCode]
Order By SP.SalesYTD, [PostalCode] DESC

-- 22.
Select BEC.ContactTypeID, CT.Name as ctpyename,count(BEC.ContactTypeID) as [No Contact] 
from [Person].[BusinessEntityContact] As BEC
join [Person].[ContactType] as CT
ON BEC.ContactTypeID = CT.ContactTypeID 
Group BY BEC.ContactTypeID, CT.Name
Having count(BEC.ContactTypeID) >= 100
Order By count(BEC.ContactTypeID) DESC

-- 23.
-- Not Accurate 
Select cast(EPH.ModifiedDate as date) as FromDate,(PP.[FirstName] + ' ' + PP.[MiddleName] + ' ' + PP.[LastName]) As [Name in Full], (EPH.Rate*40) As [Salary in a Week] from [Person].[Person] As PP
 Join [HumanResources].[EmployeePayHistory] As EPH
ON PP.BusinessEntityID = EPH.BusinessEntityID
Order By [Name in Full] ASC

-- 24.
-- Not Accurate 
Select cast(EPH.ModifiedDate as date) as FromDate,concat(PP.[FirstName],  ' ' + PP.[MiddleName], ' ' + PP.[LastName]) As [Name in Full], (EPH.Rate*40) As [Salary in a Week] 
from [Person].[Person] As PP
 Join [HumanResources].[EmployeePayHistory] As EPH
ON PP.BusinessEntityID = EPH.BusinessEntityID
Order By [Name in Full] ASC

-- 25.
Select [SalesOrderID],[ProductID],[OrderQty],
       sum([OrderQty])Over(Partition By [SalesOrderID] Order By [SalesOrderID]) as [Total Quantity],
       avg(cast([OrderQty] as Decimal(9,2))) Over(Partition By [SalesOrderID] Order By [SalesOrderID]) as [Avg Quantity],
       count([OrderQty]) Over(Partition By [SalesOrderID] Order By [SalesOrderID]) as [No of Orders],
	   min([OrderQty]) Over(Partition By [SalesOrderID] Order By [SalesOrderID]) as [Min Quantity],
	   max([OrderQty]) Over(Partition By [SalesOrderID] Order By [SalesOrderID]) as [Max Quantity]
from [Sales].[SalesOrderDetail]
Where [SalesOrderID] = 43659 or [SalesOrderID] = 43664




      

