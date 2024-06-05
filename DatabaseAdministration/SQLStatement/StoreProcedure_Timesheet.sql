USE [GraduateDB]
GO

SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE PROCEDURE [dbo].[TimeSheetErrorRows]
AS
BEGIN
    SET NOCOUNT ON;

    -- Insert rows with errors into TimesheetErrors
    INSERT INTO [dbo].[TimesheetErrors] (
        [Date], [DayofWeek], [Consultant], [Client], [ClientProjectName],
        [Description], [BillableorNonBillable], [Comments], [TotalHours],
        [StartTime], [EndTime]
    )
    SELECT
        [Date], [DayOfWeek], [Consultant], [Client], [ClientProjectName],
        [Description], [BillableOrNonBillable], [Comments], [TotalHours],
        [StartTime], [EndTime]
    FROM [dbo].[Timesheet] t
    WHERE
        NOT EXISTS (
            SELECT 1 FROM dbo.Consultant c
            WHERE c.Consultant = t.Consultant
        )
        OR
        NOT EXISTS (
            SELECT 1 FROM dbo.Client cl
            WHERE cl.Client = t.Client
        )
        OR
        NOT EXISTS (
            SELECT 1 FROM dbo.Description d
            WHERE d.Description = t.Description
        )
        OR
        NOT EXISTS (
            SELECT 1 FROM dbo.Billable b
            WHERE b.Billable = t.BillableOrNonBillable
        );

    -- Delete the rows with errors from the Timesheet table
    DELETE FROM [dbo].[Timesheet]
    WHERE
        NOT EXISTS (
            SELECT 1 FROM dbo.Consultant c
            WHERE c.Consultant = [Timesheet].Consultant
        )
        OR
        NOT EXISTS (
            SELECT 1 FROM dbo.Client cl
            WHERE cl.Client = [Timesheet].Client
        )
        OR
        NOT EXISTS (
            SELECT 1 FROM dbo.Description d
            WHERE d.Description = [Timesheet].Description
        )
        OR
        NOT EXISTS (
            SELECT 1 FROM dbo.Billable b
            WHERE b.Billable = [Timesheet].BillableOrNonBillable
        );
END;
GO
