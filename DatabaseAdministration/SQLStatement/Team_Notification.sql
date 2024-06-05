CREATE PROCEDURE [dbo].[SSISTeamsNotification]
AS
BEGIN
    DECLARE @url NVARCHAR(500), @body NVARCHAR(MAX), @response INT;
    -- Set the Teams webhook URL
    SET @url = 'https://northerndata.webhook.office.com/webhookb2/2febf530-3373-447a-ad7e-d3f06a4d642f@174c7352-9c5c-4558-b848-be140b444e7d/IncomingWebhook/4c9c0eb230c943f79de22db94a6a0ab4/2dffc6ec-6b7a-448a-9250-5231830b2de5';

    -- JSON payload for the notification
    SET @body = '{"text": "SSIS package has Failed."}';
    -- Send the POST request
    EXEC sp_OACreate 'MSXML2.ServerXMLHTTP', @response OUT;
    EXEC sp_OAMethod @response, 'Open', NULL, 'POST', @url, 'false';
    EXEC sp_OAMethod @response, 'setRequestHeader', NULL, 'Content-Type', 'application/json';
    EXEC sp_OAMethod @response, 'send', NULL, @body;
    EXEC sp_OADestroy @response;
END;
GO

exec SSISTeamsNotification

EXEC sp_configure 'show advanced options', 1;
RECONFIGURE;
go
 
EXEC sp_configure 'Ole Automation Procedures', 1;
RECONFIGURE;
drop proc SSISTeamsNotification

CREATE PROCEDURE [dbo].[SSISTeamsNotification2]
AS
BEGIN
    DECLARE @url NVARCHAR(500), @body NVARCHAR(MAX), @response INT;
    -- Set the Teams webhook URL
    SET @url = 'https://northerndata.webhook.office.com/webhookb2/2febf530-3373-447a-ad7e-d3f06a4d642f@174c7352-9c5c-4558-b848-be140b444e7d/IncomingWebhook/4c9c0eb230c943f79de22db94a6a0ab4/2dffc6ec-6b7a-448a-9250-5231830b2de5';

    -- JSON payload for the notification
    SET @body = '{"text": "SSIS package has completed successfully."}';
    -- Send the POST request
    EXEC sp_OACreate 'MSXML2.ServerXMLHTTP', @response OUT;
    EXEC sp_OAMethod @response, 'Open', NULL, 'POST', @url, 'false';
    EXEC sp_OAMethod @response, 'setRequestHeader', NULL, 'Content-Type', 'application/json';
    EXEC sp_OAMethod @response, 'send', NULL, @body;
    EXEC sp_OADestroy @response;
END;
GO