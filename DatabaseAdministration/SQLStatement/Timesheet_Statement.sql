--------------------------------------------------
Select * from [dbo].[Consultant]
Select * from [dbo].[DimConsultant]

Select * from [dbo].[Client]
Select * from [dbo].[DimClient]

Select * from [dbo].[Billable]
Select * from [dbo].[Description]

Select * from [dbo].[Project]
Select * from [dbo].[DimProject]

Select * from [dbo].[DimDate]

Select * from [dbo].[TimesheetFact]

Select * from StagingTimesheet

truncate table [dbo].[StagingTimesheet]
truncate table [dbo].[TimesheetFact]
---------------------------------------------
truncate table [dbo].[DimConsultant]
truncate table [dbo].[Consultant]

Truncate table [dbo].[Client]
Truncate table [dbo].[DimClient]

Truncate table [dbo].[Project]
Truncate table [dbo].[DimProject]

Truncate table [dbo].[Description]
Truncate table [dbo].[Billable]
truncate table [dbo].[StagingTimesheet]
-----------------------------------------------------------
select * from [dbo].[TimesheetErrors]
select * from [dbo].[DimConsultant]
select  ConsultantKey,ClientKey,[Month], Count([TotalHours]) as TotalHours from [dbo].[TimesheetFact]
Group by ConsultantKey,ClientKey,[Month]

Select * from [dbo].[TimesheetFact]
/*
update a
set a.ExpirationDate = getdate()
from DimConsultant a inner join ConsultantInsert b
on a.ConsultantID = b.ConsultantID
where a.ExpirationDate is null
*/
--------------------------------------------------

CREATE TABLE DimProject (
    ProjectKey UNIQUEIDENTIFIER PRIMARY KEY DEFAULT NEWID(),
    ClientKey UNIQUEIDENTIFIER NOT NULL,
    ProjectID INT,
    ProjectName VARCHAR(200) NOT NULL,
    EffectiveDate DATE NOT NULL,
    ExpirationDate DATE NULL,
    FOREIGN KEY (ClientKey) REFERENCES DimClient(ClientKey)
);


CREATE TABLE Project (
	ProjectID INT,
    ProjectName VARCHAR(200) NOT NULL
);


------------------------------------------------
CREATE TABLE Description (
    DescriptionID INt,
    Description NVARCHAR(255) NULL
);

-----------------------------------------------

CREATE TABLE Billable (
    BillableID INT IDENTITY(1,1) PRIMARY KEY,
    Billable NVARCHAR(12) NULL
);

--------------------------------------------------------------
CREATE TABLE TypeOfLeave(
    TypeOfLeaveID INT PRIMARY KEY IDENTITY(1,1),
    TypeOfLeave VARCHAR(50)
);
-------------------------------------------------------------
CREATE TABLE [dbo].[ChargeableToClient] (
    [ChargeableToClientID] INT IDENTITY(1,1) PRIMARY KEY,
    [Chargeable] NVARCHAR(3)  NULL
);

--------------------------------------------------------------
CREATE TABLE [dbo].[Type] (
    [TypeID] INT IDENTITY(1,1) PRIMARY KEY,
    [TypeName] NVARCHAR(10)  NULL
);
--------------------------------------------------------------
Select * from [dbo].[Billable]
Select * from [dbo].[Client]
Select * from [dbo].[Consultant]
select * from [dbo].[Description]

Select * from [dbo].[Timesheet]
Select * from [dbo].[TimesheetErrors]

Truncate table [dbo].[Timesheet]
--------------------------------------------------------------

Select * From [dbo].[TypeOfLeave]
Select * from [dbo].[Leave]
Select * from [dbo].[LeaveErrors]

Truncate table [dbo].[Leave]
------------------------------------------------------------
Select * from [dbo].[ExpenseClaim]
Select * from [dbo].[ChargeableToClient]
Select * from [dbo].[Type]

Select * from [dbo].[ExpenseClaimErrors]

Truncate table [dbo].[ExpenseClaim]

------------------------------------------------------------

Select * from [dbo].[audit_log]

-----------------------------------------------------------

CREATE TABLE TimesheetFact (
    TimesheetID INT PRIMARY KEY ,
    [DateID] DATE NOT NULL,
	Month nvarchar(9),
    DayOfWeek nvarchar(10),
   
    Description nvarchar(max),
    [BillableID]
    Comments  nvarchar(max),
    TotalHours Time(0),
    StartTime TIME(0),
    EndTime TIME(0)
    FOREIGN KEY (ConsultantID) REFERENCES Consultant(ConsultantID)
);

-------------------------------------------

Select * from [dbo].[TimesheetFact]
