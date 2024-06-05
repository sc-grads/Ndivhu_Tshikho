USE [GraduateDB]
GO

/****** Object:  StoredProcedure [dbo].[LeaveErrorRows]    Script Date: 5/23/2024 3:34:14 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO


CREATE PROCEDURE [dbo].[LeaveErrorRows]
AS
BEGIN
    SET NOCOUNT ON;

    -- Insert rows with errors into LeaveErrors
    INSERT INTO [dbo].[LeaveErrors](
        [Consultant], [TypeOfLeave], [StartDate], [EndDate], [NumberOfDays], [ApprovalObtained], [SickNote]
    )
    SELECT
        [Consultant], [TypeOfLeave], [StartDate], [EndDate], [NumberOfDays], [ApprovalObtained], [SickNote]
    FROM [dbo].[Leave] l
    WHERE
        NOT EXISTS (
            SELECT 1 FROM [dbo].[Consultant] c
            WHERE c.ConsultantName = l.Consultant
        )
        OR
        NOT EXISTS (
            SELECT 1 FROM [dbo].[TypeOfLeave] ty
            WHERE ty.TypeOfLeave = l.TypeOfLeave
        );

    -- Delete the rows with errors from the Leave table
    DELETE FROM [dbo].[Leave]
    WHERE
        NOT EXISTS (
            SELECT 1 FROM [dbo].[Consultant] c
            WHERE c.ConsultantName = [dbo].[Leave].Consultant
        )
        OR
        NOT EXISTS (
            SELECT 1 FROM [dbo].[TypeOfLeave] ty
            WHERE ty.TypeOfLeave = [dbo].[Leave].TypeOfLeave
        );
END;
GO

