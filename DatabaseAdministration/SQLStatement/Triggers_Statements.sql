-- Are dpecial stored procedures that are executed automatically in response to the database object,
-- database and server events.

-- Syntax 

CREATE TRIGGER [schema_name] trigger_name
ON table_name
AFTER -- {INSERT, DELETE, UPDATE}
AS sql_statement


--- Example

CREATE TABLE [dbo].[EmployeeTriggerHistory](
	[ID] [int] NULL,
	[Statement] [nchar](10) NULL
) ON [PRIMARY]

GO

CREATE TRIGGER [dbo].[EmployeeInsert] 
   ON  [dbo].[Employee] 
   AFTER INSERT
AS 
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for trigger here
	Insert into EmployeeTriggerHistory values ((select Top 1 (EmpID) from employee),'Insert')


END

GO

INSERT INTO Employee (EmpID, EmpName, EmpTitle) values (7, 'Craig', 'Manager')
select * from [dbo].[EmployeeTriggerHistory]