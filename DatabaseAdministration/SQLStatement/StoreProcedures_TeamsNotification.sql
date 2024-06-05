USE [GraduateDB]
GO
/****** Object:  StoredProcedure [dbo].[SSISTeamsNotification2]    Script Date: 5/15/2024 6:02:39 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

Create PROCEDURE [dbo].[SSISTeamsNotificationSuccess]
AS
BEGIN
    DECLARE @url NVARCHAR(500), @body NVARCHAR(MAX), @response INT;
    DECLARE @totalConsultants INT, @consultantsWithTimeSheet INT, @consultantsWithoutTimeSheet INT;
    
    -- Set the Teams webhook URL
    SET @url = 'https://northerndata.webhook.office.com/webhookb2/2febf530-3373-447a-ad7e-d3f06a4d642f@174c7352-9c5c-4558-b848-be140b444e7d/IncomingWebhook/4c9c0eb230c943f79de22db94a6a0ab4/2dffc6ec-6b7a-448a-9250-5231830b2de5';
    
    -- Calculate the number of consultants
    SELECT @totalConsultants = COUNT(*) FROM Consultant;
    
    -- Calculate the number of consultants who have loaded their time sheet
    SELECT @consultantsWithTimeSheet = COUNT(DISTINCT c.ConsultantID)
    FROM Consultants c
    JOIN Timesheet t ON c.Consultant = t.Consultant
    WHERE t.Date IS NOT NULL;

    -- Calculate the number of consultants who haven't loaded their time sheet
    SET @consultantsWithoutTimeSheet = @totalConsultants - @consultantsWithTimeSheet;
    
    -- JSON payload for the notification
    SET @body = '{
        "text": "SSIS package has run successfully. Here is the time sheet summary:",
        "sections": [
            {
                "activityTitle": "Consultants Timesheet Summary",
                "facts": [
                    { "name": "Total Consultants", "value": "' + CAST(@totalConsultants AS NVARCHAR) + '" },
                    { "name": "Time Sheets Loaded", "value": "' + CAST(@consultantsWithTimeSheet AS NVARCHAR) + '" },
                    { "name": "Time Sheets Not Loaded", "value": "' + CAST(@consultantsWithoutTimeSheet AS NVARCHAR) + '" }
                ],
                "potentialAction": [
                    {
                        "@type": "OpenUri",
                        "name": "View Dashboard",
                        "targets": [
                            { "os": "default", "uri": "http://localhost:5601/app/r/s/upBLk" }
                        ]
                    }
                ]
            }
        ]
    }';
    
    -- Send the POST request
    EXEC sp_OACreate 'MSXML2.ServerXMLHTTP', @response OUT;
    EXEC sp_OAMethod @response, 'Open', NULL, 'POST', @url, 'false';
    EXEC sp_OAMethod @response, 'setRequestHeader', NULL, 'Content-Type', 'application/json';
    EXEC sp_OAMethod @response, 'send', NULL, @body;
    EXEC sp_OADestroy @response;
END;
