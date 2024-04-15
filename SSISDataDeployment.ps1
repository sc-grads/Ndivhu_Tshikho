        # Variables
        $SSISNamespace = "Microsoft.SqlServer.Management.IntegrationServices"
        $TargetServerName = "DESKTOP-PL72RR2"
        $TargetFolderName = "Data Flow Task"
        $ProjectFilePath = "C:\Users\NdivhudzannyiT\Documents\Ndivhu_Tshikho\DatabaseAdministration\SSIS\Data Flow Task\bin\Development\Data Flow Task.ispac"
        $ProjectName = "Data Flow Task"

        Add-Type -Path "C:\Program Files (x86)\Microsoft SQL Server Management Studio 19\Common7\IDE\CommonExtensions\Microsoft\SSIS\160\Binn\150References\SM0\Microsoft.SqlServer.Dmf.Common.dll"

        # Load the IntegrationServices assembly
        $loadStatus = [System.Reflection.Assembly]::Load("Microsoft.SQLServer.Management.IntegrationServices, "+
            "Version=16.0.0.0, Culture=neutral, PublicKeyToken=89845dcd8080cc91, processorArchitecture=MSIL")

        # Create a connection to the server
        $sqlConnectionString = "Data Source=" + $TargetServerName + ";Initial Catalog=master;Integrated Security=SSPI;"
        $sqlConnection = New-Object System.Data.SqlClient.SqlConnection $sqlConnectionString

        # Create the Integration Services object
        $integrationServices = New-Object $SSISNamespace".IntegrationServices" $sqlConnection

        # Get the Integration Services catalog
        $catalog = $integrationServices.Catalogs["SSISDB"]

        # Create the target folder
        $folder = New-Object $SSISNamespace".CatalogFolder" ($catalog, $TargetFolderName, "Folder description")
        $folder.Create()

        Write-Host "Deploying " $ProjectName " project ..."

        # Read the project file and deploy it
        [byte[]] $projectFile = [System.IO.File]::ReadAllBytes($ProjectFilePath)
        $folder.DeployProject($ProjectName, $projectFile)

        Write-Host "Done."