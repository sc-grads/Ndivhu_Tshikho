DECLARE @ProjectBinary as varbinary(max)  
DECLARE @operation_id as bigint  
Set @ProjectBinary = (SELECT * FROM OPENROWSET(BULK 'C:\Users\NdivhudzannyiT\Documents\Ndivhu_Tshikho\DatabaseAdministration\SSIS\Practice Activity 2\bin\Development\Practice Activity 2.ispac', SINGLE_BLOB) as BinaryData)  

Exec catalog.deploy_project @folder_name = 'CustomerProject', @project_name = 'Practice Activity 2', @Project_Stream = @ProjectBinary, @operation_id = @operation_id out  


