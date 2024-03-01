SELECT 
FirstName+ ' ' + LastName AS FullName,
TerritoryName,
TerritoryGroup,
SalesQuota,
SalesYTD,
SalesLastYear
INTO salesstaff
From 
Sales.vSalesPerson

------------------------------------------------------------------------------------

drop table salesstaff;

------------------------------------------------------------------------------------


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

UPDATE SalesStaff SET salesquota = sp.salesquota
From SalesStaff ss
Inner join sales.vSalesPerson sp
ON ss.FullName = sp.FirstName +' '+ sp.LastName

SELECT * From salesstaff