--List all columns in a tablle.
SELECT *
From table_name

--Specify column in a table and the order does not matter.
SELECT column1, column2
From table_name

/*
##SELECT- Indicates that you want to retrieve data from a database.

## (*)- Denotes all columns, it means that you want to retrieve all columns from the specified table.

## column1, column2 - These are the names of the columns you want to retrieve data from.
## Only data from columns "column1" and "column2" will be selected.

## From - Specifies the table from which you want to retrieve data

table_name - This is the name of the table from which you want to retrieve data.
[Person].[Address] - "Person" is the schema or database name, and "Address" is the table name.
*/

--Example--

SELECT *
From Person.Address

SELECT addressid,city,modifieddate
From [Person].[Address]

-----------WHERE clause------------
-----is used to specify a condition and to filter the rows.

SELECT * From [Person].[Address] WHERE [PostalCode] = '98011'
SELECT * From [Person].[Address] WHERE [PostalCode] != '98011'
SELECT * From [Person].[Address] WHERE [PostalCode] <> '98011'

----count(*) function counts the number of rows that match the specified conditions.
SELECT count(*) From [Person].[Address] WHERE [PostalCode] = '98011'

----------ORDER BY clause----------
-----used to sort data in ascending order, based on one or more columns.
-----some database sort the query results in an ascending order by default.

SELECT * From [HumanResources].[EmployeePayHistory] order by Rate
SELECT * From [HumanResources].[EmployeePayHistory] order by Rate DESC
SELECT * From [HumanResources].[EmployeePayHistory] order by Rate ASC

---------WHERE and ORDER By clause--------
SELECT * From [HumanResources].[EmployeePayHistory] WHERE ModifiedDate >= '2010-06-30' order by ModifiedDate DESC

---------WHERE, GROUP BY and HAVING--------

------Group by clause  HAVING follow GROUP by and also precede the ORDER by if used.----
------HAVING clause enables you to specify coditions,on groups created by the GROUP by clause.

SELECT Count(1) As CountOfProduct, Color From [Production].[Product] WHERE color = 'yellow' Group by Color 
SELECT Count(1) As CountOfProduct, Color From [Production].[Product] Group by Color HAVING Color = 'yellow'
SELECT Count(1) As CountOfProduct, Color,Size From [Production].[Product] Group by Color,Size HAVING Size >= '44' 
