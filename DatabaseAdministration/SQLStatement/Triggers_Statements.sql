Use AdventureWorks2022
Go

-- Are dpecial stored procedures that are executed automatically in response to the database object,
-- database and server events.

-- Syntax 

CREATE TRIGGER [schema_name] trigger_name
ON table_name
AFTER -- {INSERT, DELETE, UPDATE}
AS sql_statement


SELECT TOP (1000) [EmpName]
      ,[EmpTitle]
      ,[EmpID]
  FROM [AdventureWorks2022].[dbo].[Employee]


--- Example

CREATE TABLE [dbo].[EmployeeTriggerHistory](
	[ID] [int] NULL,
	[Statement] [nchar](10) NULL
) ON [PRIMARY]

select * from [dbo].[EmployeeTriggerHistory]
--drop table [dbo].[EmployeeTriggerHistory]
GO
--drop TRIGGER [dbo].[EmployeeInsert] 
CREATE TRIGGER [dbo].[EmployeeInsert] 
   ON  [dbo].[Employee]
   AFTER INSERT
AS 
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for trigger here
	Insert into EmployeeTriggerHistory values ((select Top 100(EmpID) from Employee), 'Insert')

END
GO

--insert into [Employee] (EmpID,[EmpName],[EmpTitle]) values (15,'Queen','Manager')
select * from [dbo].[EmployeeTriggerHistory]