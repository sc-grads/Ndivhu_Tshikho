USE [GraduateDB]
GO

SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE PROCEDURE [dbo].[ExpenseClaimErrorRows]
AS
BEGIN
    SET NOCOUNT ON;

    -- Insert rows with errors into ExpenseClaimErrors
    INSERT INTO [dbo].[ExpenseClaimErrors](
        [Date], [Consultant], [ExpenseDescription], [Type], [ChargeableToClient], [ClientName], [ZARCost], [Slip]
    )
    SELECT
        [Date], [Consultant], [ExpenseDescription], [Type], [ChargeableToClient], [ClientName], [ZARCost], [Slip]
    FROM [dbo].[ExpenseClaim] ec
    WHERE
        NOT EXISTS (
            SELECT 1 FROM [dbo].[Consultant] c
            WHERE c.Consultant = ec.Consultant
        )
        OR
        NOT EXISTS (
            SELECT 1 FROM [dbo].[Type] t
            WHERE t.[TypeName] = ec.Type
        )
        OR
        NOT EXISTS (
            SELECT 1 FROM [dbo].[ChargeableToClient] cc
            WHERE cc.[Chargeable] = ec.ChargeableToClient
        )
        OR
        NOT EXISTS (
            SELECT 1 FROM [dbo].[Client] cl
            WHERE cl.[Client] = ec.ClientName
        );

    -- Delete the rows with errors from the ExpenseClaim table
    DELETE FROM [dbo].[ExpenseClaim]
    WHERE
        NOT EXISTS (
            SELECT 1 FROM [dbo].[Consultant] c
            WHERE c.Consultant = [dbo].[ExpenseClaim].Consultant
        )
        OR
        NOT EXISTS (
            SELECT 1 FROM [dbo].[Type] t
            WHERE t.[TypeName] = [dbo].[ExpenseClaim].Type
        )
        OR
        NOT EXISTS (
            SELECT 1 FROM [dbo].[ChargeableToClient] cc
            WHERE cc.[Chargeable] = [dbo].[ExpenseClaim].ChargeableToClient
        )
        OR
        NOT EXISTS (
            SELECT 1 FROM [dbo].[Client] cl
            WHERE cl.[Client] = [dbo].[ExpenseClaim].ClientName
        );
END;
GO
