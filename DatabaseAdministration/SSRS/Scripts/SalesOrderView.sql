CREATE VIEW SalesOrderAnalysis AS
SELECT 
    so.CustomerID,
    so.OrderDate,
    p.Name AS ProductName,
    sod.OrderQty
FROM 
    Sales.SalesOrderHeader so
JOIN 
    Sales.SalesOrderDetail sod ON so.SalesOrderID = sod.SalesOrderID
JOIN 
    Production.Product p ON sod.ProductID = p.ProductID;
