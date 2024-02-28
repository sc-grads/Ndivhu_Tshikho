
## CREATE TABLE--This SQL command is used to create a new table in the database
## [AdventureWorks2022].[Sales].[Visit]-- This specifies the fully qualified name of the table. 
## "AdventureWorks2022" is the database name, "Sales" is the schema name, and "Visit" is the table name.

## visit_id INT PRIMARY KEY IDENTITY (1,1)--This defines the first column of the table named "visit_id" with the following properties
## INT-- Specifies the data type of the column as integer.
## PRIMARY KEY --Indicates that this column is the primary key for the table, ensuring uniqueness and 
## --providing a unique identifier for each row.
## IDENTITY (1,1) -- Specifies that the column is an identity column, which automatically generates 
## --incremental values starting from 1 with a seed of 1 and an increment of 1 for each new row inserted into the table.

## store_id INT NOT NULL--This line defines the store_id column with the following properties
## INT--Specifies the data type of the column as integer.
## NOT NULL--Specifies that this column cannot contain null values.
## FOREIGN KEY (store_id) REFERENCES Sales.Storenew(store_id) 
## --This line creates a foreign key constraint on the store_id column, 
## --referencing the store_id column in the Sales.Storenew table. 
## --This ensures referential integrity by enforcing that the values in the store_id column of 
## --the Visit table must exist in the store_id column of the Sales.Storenew table.

CREATE TABLE [AdventureWorks2022].[Sales].[Visit](
visit_id INT PRIMARY KEY IDENTITY (1,1),
first_name VARCHAR (50) NOT NULL,
last_name VARCHAR (50) NOT NULL,
visited_time  DATETIME,
phone VARCHAR(20),
store_id INT NOT NULL,
FOREIGN KEY (store_id) REFERENCES Sales.Storenew(store_id)
)

SELECT * From [AdventureWorks2022].[Sales].[Visit]