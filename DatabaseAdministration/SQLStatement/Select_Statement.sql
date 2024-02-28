
##List all columns in a tablle.
SELECT *
From table_name

##Specify column in a table and the order does not matter.
SELECT column1, column2
From table_name

##SELECT- Indicates that you want to retrieve data from a database.

## (*)- Denotes all columns, it means that you want to retrieve all columns from the specified table.

## column1, column2 - These are the names of the columns you want to retrieve data from.
## Only data from columns "column1" and "column2" will be selected.

## From - Specifies the table from which you want to retrieve data

## table_name - This is the name of the table from which you want to retrieve data.
## [Person].[Address] - "Person" is the schema or database name, and "Address" is the table name.

###Example

SELECT *
From Person.Address

SELECT addressid,city,modifieddate
From [Person].[Address]



