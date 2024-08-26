--1. 
Create View vw_DuplicateSalesPerson
--Ndichudzannyi Israel Tshikhovhokhovho
AS
Select FullName from SalesPerson
Group By FullName
Having count(*) > 1;

Select * from vw_DuplicateSalesPerson

--2.
Create Procedure sp_SalesAmountbySalesPerson
--Ndivhudzannyi Israel Tshikhovhokhovho
AS
BEGIN
Select SP.FullName, 
       sum(SD.SalesAmount) as TotalSalesAmount
from 
SalesPerson SP
inner join 
SalesData SD
On SP.SalesPersonID = SD.SalesPersonID
Group By SP.FullName
Order By TotalSalesAmount DESC;
END

Exec sp_SalesAmountbySalesPerson

--3.

CREATE VIEW vw_SalesData
--Ndivhudzannyi Israel Tshikhovhokhovho
AS 
Select SD.SalesDate,SP.FullName,C.CustomerName,SD.SalesAmount
from 
SalesPerson SP
inner join 
SalesData SD
On SP.SalesPersonID = SD.SalesPersonID
inner join
Customer C
On SD.CustomerID = C.CustomerID

--4.
CREATE FUNCTION udf_TrimString
--Ndivhudzannyi Israel Tshikhovhokhovho
(
  @string nvarchar(255)
)
returns nvarchar(255)
AS
Begin
 return LTRIM(RTRIM(@string));
End;
Select dbo.udf_TrimString(' Hello Sir! ') as Trimmed;