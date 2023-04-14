$RGName = "ContosoResourceGroup"
#create resource group if it doesnt exist
#create resource group if it doesnt exist
New-AzResourceGroup -Name $RGName -Location "eastus"
New-AzResourceGroupDeployment -ResourceGroupName $RGName -TemplateFile azuredeploy.json -TemplateParameterFile azuredeploy.parameters.json
New-AzResourceGroupDeployment -ResourceGroupName $RGName -TemplateFile azuredeploy.json -TemplateParameterFile azuredeploy.parameters.json

$RGName = "ContosoResourceGroup"

New-AzResourceGroupDeployment -ResourceGroupName $RGName -TemplateFile CoreServicesVMazuredeploy.json -TemplateParameterFile CoreServicesVMazuredeploy.parameters.json

$RGName = "ContosoResourceGroup"

New-AzResourceGroupDeployment -ResourceGroupName $RGName -TemplateFile ManufacturingVMazuredeploy.json -TemplateParameterFile ManufacturingVMazuredeploy.parameters.json

Test-NetConnection 10.20.20.4 -port 3389

Test-NetConnection 10.20.20.4 -port 3389'
