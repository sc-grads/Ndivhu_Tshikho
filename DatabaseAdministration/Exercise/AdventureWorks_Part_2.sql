USE AdventureWorks2022
GO
-- AdventureWorks Part-I

-- 26.Write a query in SQL to find the sum, average, and number of order quantity 
--    for those orders whose ids are 43659 and 43664 and product id starting with '71'. 
--    Return SalesOrderID, OrderNumber,ProductID, OrderQty, sum, average, and number of order quantity.

Select SalesOrderID,ProductID, OrderQty, 
       sum([OrderQty])Over(Partition By [SalesOrderID] Order By [SalesOrderID]) as [Total Quantity],
       avg(cast([OrderQty] as Decimal(10,4))) Over(Partition By [SalesOrderID] Order By [SalesOrderID]) as [Avg Quantity],
       count([OrderQty]) Over(Partition By [SalesOrderID] Order By [SalesOrderID]) as [No of Orders]
from [Sales].[SalesOrderDetail]
Where ProductID like '71%' 
--Where [SalesOrderID] = 43659 and [SalesOrderID] = 43664