---Is a batch of statements grouped as alogical unit and stored in the database.
--Is a code in SQL that can be stored for later used and can be used many times.

-- Syntax of Stored Procedures

CREATE PROCEDURE procedure_name
AS sql_statement
GO
EXEC procedure_name

---Example with no parameters.

CREATE PROCEDURE SelctAllPersonAddress
AS 
SELECT * FROM [Person].[Address]
GO
EXEC SelctAllPersonAddress

---Example with parameters.

CREATE PROCEDURE SelctAllPersonAddressWithPara (@city nvarchar(30))
AS 
SELECT * FROM [Person].[Address] WHERE City= @city
GO
EXEC SelctAllPersonAddressWithPara @city = 'New York'


