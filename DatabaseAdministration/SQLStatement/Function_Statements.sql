

-- is a set of SQL Statement that perform a specific task.

--Built -In Functions---
-- Are grouped into different types depending upon their functionality 


--1. Scalar Functions
-- operate on a single value and return a single value 

print upper('ndivhu')
print lower('NDIVHU')
print convert(int, 16.48)

-- 2. Date and Time gunctions 
-- Related to date and time.

print getdate()
print day(getdate())
print month(getdate())

-- 3. Aggregate Functions 
-- Operate on a collection of values and return a single vale
-- max(), min(), avg(), count()

SELECT max(rate) from [HumanResources].[EmployeePayHistory]

SELECT min(rate) from [HumanResources].[EmployeePayHistory]

SELECT count(rate) from [HumanResources].[EmployeePayHistory]


-- User- Defined functions
-- Created by the user in the system database or in a user-defined database.

SELECT *From [Person].[Person]

Create function [dbo].[fnGetEmpFullName]
( @FirstName varchar(50), @LastName varchar(50))
returns varchar(101)
As
begin
return (select @FirstName + ' '+@LastName);
end
GO

select dbo.fnGetEmpFullName (firstname,lastname) as Fullname from [Person].[Person]
 
/*
create function [dbo].[fnGetMulEmployee]()
returns @Emp Table
(
Empid int,
EmpName varchar(50),
SaleNumber int
)
As
Begin
 Insert into @Emp Select e.EmpID,e.EmpName,e.SaleNumber from Sales e;
--Now update sales number of employee
 update @Emp set SaleNumber= 25000 where EmpID=11;
--It will update only in @Emp table not in Original Employee table
return
end 
GO

SELECT * From Sales

select * from Emp
*/