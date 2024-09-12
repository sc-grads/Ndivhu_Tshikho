USE AdventureWorks2022
GO
-- AdventureWorks Part-I

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
Select [ProductID], [ProductNumber], [Name]  as [Profile Name]
From [Production].[Profile]
Where [SellStartDate] is not null and [ProductLine] like 'T%'
Order By [Name]

-- 5.

Select [SalesOrderID], [CustomerID], [OrderDate], [SubTotal],
       ([TaxAmt]/[SubTotal])* 100 AS Tax_Percent 
from [Sales].[SalesOrderHeader]
Order By  [SubTotal] DESC

-- 6.
Select Distinct JobTitle 
From [HumanResources].[Employee]

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
Select P.[BusinessEntityID], P.[FirstName], P.[LastName], PP.[PhoneNumber] as [Person_Phone] 
from [Person].[Person] As P
Join [Person].[PersonPhone] As PP
ON P.BusinessEntityID = PP.BusinessEntityID
Where P.[LastName] Like 'L%'
Order By P.[LastName] , P.[FirstName]

-- 12.

Select [SalesPersonID],[CustomerID], sum([SubTotal]) as [Sum_SubTotal] 
from [Sales].[SalesOrderHeader]  
Where [SalesPersonID] is NOT NULL
Group By rollup ([SalesPersonID],[CustomerID])


-- 13. 
 
Select [LocationID],[Shelf], sum([Quantity] ) as TotalQuantity 
from [Production].[ProductInventory]
Group By Cube([LocationID], [Shelf])
Order BY [LocationID] 

-- 14.

select [LocationID],[Shelf], 
       sum([Quantity] ) As TotalQuantity 
from [Production].[ProductInventory]
Group By rollup ([LocationID],[Shelf])
Order By [LocationID],[Shelf]

-- 15. 

Select [LocationID], sum([Quantity] ) as TotalQuantity 
from [Production].[ProductInventory]
Group By rollup([LocationID])


-- 16. 

Select (PA.City) as city, count(BEA.BusinessEntityID) as noofemployees 
from [Person].[Address] As PA
Join [Person].[BusinessEntityAddress] as BEA
ON PA.AddressID = BEA.AddressID
Group By PA.City 
Order By PA.City ASC

-- 17.
Select  Year([OrderDate]) as [Year], sum([TotalDue]) as [Order Amount]  
from [Sales].[SalesOrderHeader]
Group By Year([OrderDate])
Order By Year([OrderDate])

-- 18.
Select  Year([OrderDate]) as YearForOrderDate,
        sum([TotalDue]) as [OrderDueAmount]  
from [Sales].[SalesOrderHeader]
Where Year([OrderDate]) <= '2016' 
Group By Year([OrderDate])
Order By Year([OrderDate]) 

-- 19.
Select[ContactTypeID], [Name]  from [Person].[ContactType]
Where [Name]  Like '%Manager' 
Order By [Name]  DESC

-- 20.

Select PP.BusinessEntityID , LastName, FirstName
From [Person].[ContactType] as CT
     inner join [Person].[BusinessEntityContact] as BEC
ON  CT.ContactTypeID = BEC.ContactTypeID
     inner join [Person].[Person] As PP
ON  BEC.PersonID = PP.BusinessEntityID
Where CT.Name = 'Purchasing Manager'
Order By PP.LastName, PP.FirstName ASC

-- 21.

select row_number() over(Partition By PA.PostalCode  Order By SP.SalesYTD) As [Row Number], 
       PP.LastName ,SP.SalesYTD, PA.PostalCode 

From [Sales].[SalesPerson] as SP
Join [Person].[Person] As PP
On SP.BusinessEntityID = PP.BusinessEntityID

Join [Person].[Address] AS PA
ON PP.BusinessEntityID = PA.AddressID

WHERE SP.TerritoryID is NUll and SP.SalesYTD <> 0
Order By PA.PostalCode 


-- 22.
Select BEC.ContactTypeID, CT.Name as ctpyename,count(BEC.ContactTypeID) as [No Contact] 
from [Person].[BusinessEntityContact] As BEC
join [Person].[ContactType] as CT
ON BEC.ContactTypeID = CT.ContactTypeID 
Group BY BEC.ContactTypeID, CT.Name
Having count(BEC.ContactTypeID) >= 100
Order By count(BEC.ContactTypeID) DESC

-- 23.

Select cast(EPH.ModifiedDate as date) as FromDate,
       concat(PP.[LastName], ',', ' ' + PP.[FirstName], ' ' + PP.[MiddleName]) As [NameinFull], 
	   (EPH.Rate*40) As [Salary in a Week] 
from [Person].[Person] As PP
Join [HumanResources].[EmployeePayHistory] As EPH
ON PP.BusinessEntityID = EPH.BusinessEntityID
Order By [NameinFull] ASC

-- 24.

Select cast(EPH.ModifiedDate as date) as FromDate,
       concat(PP.[LastName], ',', ' ' + PP.[FirstName], ' ' + PP.[MiddleName]) As [NameinFull], 
       (EPH.Rate*40) As [SalaryinaWeek] 
from [Person].[Person] As PP
 Join [HumanResources].[EmployeePayHistory] As EPH
ON PP.BusinessEntityID = EPH.BusinessEntityID
Order By [NameinFull] ASC


-- 25.
Select [SalesOrderID],[ProductID],[OrderQty],
       sum([OrderQty])Over(Partition By [SalesOrderID] Order By [SalesOrderID]) as [Total Quantity],
       avg(cast([OrderQty] as Decimal(10,4))) Over(Partition By [SalesOrderID] Order By [SalesOrderID]) as [Avg Quantity],
       count([OrderQty]) Over(Partition By [SalesOrderID] Order By [SalesOrderID]) as [No of Orders],
	   min([OrderQty]) Over(Partition By [SalesOrderID] Order By [SalesOrderID]) as [Min Quantity],
	   max([OrderQty]) Over(Partition By [SalesOrderID] Order By [SalesOrderID]) as [Max Quantity]
from [Sales].[SalesOrderDetail]
Where [SalesOrderID] = 43659 or [SalesOrderID] = 43664



      

