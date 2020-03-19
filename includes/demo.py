#!/usr/bin/env python
# DEMO payload...

"""
Copyright (c) 2020, Marcelo Leal
Description: The power is in the terminal...
License: MIT (see LICENSE.txt file for details)
"""

import json

rgname = "dashdemo"
vmssname = "dashdemo"
interval = 10
tenantId = "xxx"
insightsAppId = "xxx"
insightsKey = "xxx"
insightsUrl = "xxx"
insightsOneEnabled = "No"
insightsOneUrl = "xxx"
insightsOneMetric = "xxx"
insightsOneTitle = "xxx"
insightsTwoEnabled = "No"
insightsTwoUrl = "xxx"
insightsTwoMetric = "xxx"
insightsTwoTitle = "xxx"
insightsInterval = 10

#DEMO Assets...
VMSSGET_DEMO = json.dumps({"name": "dashdemo", "id": "/subscriptions/99999999-aaaa-bbbb-cccc-888888888888/resourceGroups/dashdemo/providers/Microsoft.Compute/virtualMachineScaleSets/dashdemo", "type": "Microsoft.Compute/virtualMachineScaleSets", "location": "brazilsouth", "sku": {"name": "Standard_A2", "tier": "Standard", "capacity": 1}, "properties": {"singlePlacementGroup": True, "upgradePolicy": {"mode": "Manual", "automaticOSUpgrade": False}, "virtualMachineProfile": {"osProfile": {"computerNamePrefix": "dashdemo", "adminUsername": "blackpanther", "linuxConfiguration": {"disablePasswordAuthentication": False}, "secrets": []}, "storageProfile": {"osDisk": {"vhdContainers": ["https://ababababababcdashdemosa.blob.core.windows.net/dashdemovhd", "https://ababababababcdashdemosa.blob.core.windows.net/dashdemovhd", "https://8765432123456dashdemosa.blob.core.windows.net/dashdemovhd", "https://ababababababcdashdemosa.blob.core.windows.net/dashdemovhd", "https://ababababababcdashdemosa.blob.core.windows.net/dashdemovhd"], "name": "dashdemoosdisk", "createOption": "FromImage", "caching": "ReadOnly"}, "imageReference": {"publisher": "Canonical", "offer": "UbuntuServer", "sku": "16.04.0-LTS", "version": "latest"}}, "networkProfile": {"networkInterfaceConfigurations": [{"name": "dashdemonic", "properties": {"primary": True, "ipConfigurations": [{"name": "dashdemoipconfig", "properties": {"subnet": {"id": "/subscriptions/99999999-aaaa-bbbb-cccc-888888888888/resourceGroups/VMSSDASH/providers/Microsoft.Network/virtualNetworks/dashdemovnet/subnets/dashdemosubnet"}}}]}}]}}, "provisioningState": "Succeeded", "overprovision": False, "uniqueId": "88888888-cccc-bbbb-aaaa-999999999999"}})
 
NET_DEMO = json.dumps({"value": [{"name": "dashdemopip", "id": "/subscriptions/99999999-aaaa-bbbb-cccc-888888888888/resourceGroups/VMSSDASH/providers/Microsoft.Network/publicIPAddresses/dashdemopip", "etag": "W/\'77777777-cccc-aaaa-bbbb-666666666666\'", "location": "brazilsouth", "properties": {"provisioningState": "Succeeded", "resourceGuid": "55555555-vvvv-nnnn-rrrr-444444444444", "ipAddress": "999.999.999.999", "publicIPAddressVersion": "IPv4", "publicIPAllocationMethod": "Dynamic", "idleTimeoutInMinutes": 4, "dnsSettings": {"domainNameLabel": "dashdemo", "fqdn": "dashdemo.brazilsouth.cloudapp.azure.com"}, "ipTags": [], "ipConfiguration": {"id": "/subscriptions/99999999-aaaa-bbbb-cccc-888888888888/resourceGroups/VMSSDASH/providers/Microsoft.Network/networkInterfaces/dashdemojboxnic/ipConfigurations/dashdemojboxipconfig"}}, "type": "Microsoft.Network/publicIPAddresses", "sku": {"name": "Basic"}}]})

QUOTA_DEMO = json.dumps({u"value": [{u"currentValue": 0, u"limit": 2000, u"name": {u"localizedValue": u"Availability Sets", u"value": u"availabilitySets"}, u"unit": u"Count"}, {u"currentValue": 4, u"limit": 1000, u"name": {u"localizedValue": u"Total Regional vCPUs", u"value": u"cores"}, u"unit": u"Count"}, {u"currentValue": 2, u"limit": 25000, u"name": {u"localizedValue": u"Virtual Machines", u"value": u"virtualMachines"}, u"unit": u"Count"}, {u"currentValue": 1, u"limit": 2000, u"name": {u"localizedValue": u"Virtual Machine Scale Sets", u"value": u"virtualMachineScaleSets"}, u"unit": u"Count"}, {u"currentValue": 4, u"limit": 1000, u"name": {u"localizedValue": u"Standard A0-A7 Family vCPUs", u"value": u"standardA0_A7Family"}, u"unit": u"Count"}, {u"currentValue": 0, u"limit": 100, u"name": {u"localizedValue": u"Basic A Family vCPUs", u"value": u"basicAFamily"}, u"unit": u"Count"}, {u"currentValue": 0, u"limit": 100, u"name": {u"localizedValue": u"Standard A8-A11 Family vCPUs", u"value": u"standardA8_A11Family"}, u"unit": u"Count"}, {u"currentValue": 0, u"limit": 100, u"name": {u"localizedValue": u"Standard D Family vCPUs", u"value": u"standardDFamily"}, u"unit": u"Count"}, {u"currentValue": 0, u"limit": 100, u"name": {u"localizedValue": u"Standard Dv2 Family vCPUs", u"value": u"standardDv2Family"}, u"unit": u"Count"}, {u"currentValue": 0, u"limit": 100, u"name": {u"localizedValue": u"Standard DS Family vCPUs", u"value": u"standardDSFamily"}, u"unit": u"Count"}, {u"currentValue": 0, u"limit": 100, u"name": {u"localizedValue": u"Standard DSv2 Family vCPUs", u"value": u"standardDSv2Family"}, u"unit": u"Count"}, {u"currentValue": 0, u"limit": 100, u"name": {u"localizedValue": u"Standard G Family vCPUs", u"value": u"standardGFamily"}, u"unit": u"Count"}, {u"currentValue": 0, u"limit": 100, u"name": {u"localizedValue": u"Standard GS Family vCPUs", u"value": u"standardGSFamily"}, u"unit": u"Count"}, {u"currentValue": 0, u"limit": 100, u"name": {u"localizedValue": u"Standard F Family vCPUs", u"value": u"standardFFamily"}, u"unit": u"Count"}, {u"currentValue": 0, u"limit": 100, u"name": {u"localizedValue": u"Standard FS Family vCPUs", u"value": u"standardFSFamily"}, u"unit": u"Count"}, {u"currentValue": 0, u"limit": 24, u"name": {u"localizedValue": u"Standard NV Family vCPUs", u"value": u"standardNVFamily"}, u"unit": u"Count"}, {u"currentValue": 0, u"limit": 48, u"name": {u"localizedValue": u"Standard NC Family vCPUs", u"value": u"standardNCFamily"}, u"unit": u"Count"}, {u"currentValue": 0, u"limit": 8, u"name": {u"localizedValue": u"Standard H Family vCPUs", u"value": u"standardHFamily"}, u"unit": u"Count"}, {u"currentValue": 0, u"limit": 100, u"name": {u"localizedValue": u"Standard Av2 Family vCPUs", u"value": u"standardAv2Family"}, u"unit": u"Count"}, {u"currentValue": 0, u"limit": 100, u"name": {u"localizedValue": u"Standard LS Family vCPUs", u"value": u"standardLSFamily"}, u"unit": u"Count"}, {u"currentValue": 0, u"limit": 100, u"name": {u"localizedValue": u"Standard Dv2 Promo Family vCPUs", u"value": u"standardDv2PromoFamily"}, u"unit": u"Count"}, {u"currentValue": 0, u"limit": 100, u"name": {u"localizedValue": u"Standard DSv2 Promo Family vCPUs", u"value": u"standardDSv2PromoFamily"}, u"unit": u"Count"}, {u"currentValue": 0, u"limit": 0, u"name": {u"localizedValue": u"Standard MS Family vCPUs", u"value": u"standardMSFamily"}, u"unit": u"Count"}, {u"currentValue": 0, u"limit": 100, u"name": {u"localizedValue": u"Standard Dv3 Family vCPUs", u"value": u"standardDv3Family"}, u"unit": u"Count"}, {u"currentValue": 0, u"limit": 100, u"name": {u"localizedValue": u"Standard DSv3 Family vCPUs", u"value": u"standardDSv3Family"}, u"unit": u"Count"}, {u"currentValue": 0, u"limit": 100, u"name": {u"localizedValue": u"Standard Ev3 Family vCPUs", u"value": u"standardEv3Family"}, u"unit": u"Count"}, {u"currentValue": 0, u"limit": 100, u"name": {u"localizedValue": u"Standard ESv3 Family vCPUs", u"value": u"standardESv3Family"}, u"unit": u"Count"}, {u"currentValue": 0, u"limit": 100, u"name": {u"localizedValue": u"Standard BS Family vCPUs", u"value": u"standardBSFamily"}, u"unit": u"Count"}, {u"currentValue": 0, u"limit": 100, u"name": {u"localizedValue": u"Standard FSv2 Family vCPUs", u"value": u"standardFSv2Family"}, u"unit": u"Count"}, {u"currentValue": 0, u"limit": 0, u"name": {u"localizedValue": u"Standard NDS Family vCPUs", u"value": u"standardNDSFamily"}, u"unit": u"Count"}, {u"currentValue": 0, u"limit": 0, u"name": {u"localizedValue": u"Standard NCSv2 Family vCPUs", u"value": u"standardNCSv2Family"}, u"unit": u"Count"}, {u"currentValue": 0, u"limit": 0, u"name": {u"localizedValue": u"Standard NCSv3 Family vCPUs", u"value": u"standardNCSv3Family"}, u"unit": u"Count"}, {u"currentValue": 0, u"limit": 100, u"name": {u"localizedValue": u"Standard LSv2 Family vCPUs", u"value": u"standardLSv2Family"}, u"unit": u"Count"}, {u"currentValue": 0, u"limit": 6, u"name": {u"localizedValue": u"Standard PBS Family vCPUs", u"value": u"standardPBSFamily"}, u"unit": u"Count"}, {u"currentValue": 0, u"limit": 100, u"name": {u"localizedValue": u"Standard EIv3 Family vCPUs", u"value": u"standardEIv3Family"}, u"unit": u"Count"}, {u"currentValue": 0, u"limit": 100, u"name": {u"localizedValue": u"Standard EISv3 Family vCPUs", u"value": u"standardEISv3Family"}, u"unit": u"Count"}, {u"currentValue": 0, u"limit": 8, u"name": {u"localizedValue": u"Standard DCS Family vCPUs", u"value": u"standardDCSFamily"}, u"unit": u"Count"}, {u"currentValue": 0, u"limit": 0, u"name": {u"localizedValue": u"Standard NVSv2 Family vCPUs", u"value": u"standardNVSv2Family"}, u"unit": u"Count"}, {u"currentValue": 0, u"limit": 0, u"name": {u"localizedValue": u"Standard MSv2 Family vCPUs", u"value": u"standardMSv2Family"}, u"unit": u"Count"}, {u"currentValue": 0, u"limit": 0, u"name": {u"localizedValue": u"Standard HBS Family vCPUs", u"value": u"standardHBSFamily"}, u"unit": u"Count"}, {u"currentValue": 0, u"limit": 0, u"name": {u"localizedValue": u"Standard HCS Family vCPUs", u"value": u"standardHCSFamily"}, u"unit": u"Count"}, {u"currentValue": 0, u"limit": 0, u"name": {u"localizedValue": u"Standard NVSv3 Family vCPUs", u"value": u"standardNVSv3Family"}, u"unit": u"Count"}, {u"currentValue": 0, u"limit": 24, u"name": {u"localizedValue": u"Standard NV Promo Family vCPUs", u"value": u"standardNVPromoFamily"}, u"unit": u"Count"}, {u"currentValue": 0, u"limit": 48, u"name": {u"localizedValue": u"Standard NC Promo Family vCPUs", u"value": u"standardNCPromoFamily"}, u"unit": u"Count"}, {u"currentValue": 0, u"limit": 8, u"name": {u"localizedValue": u"Standard H Promo Family vCPUs", u"value": u"standardHPromoFamily"}, u"unit": u"Count"}, {u"currentValue": 0, u"limit": 0, u"name": {u"localizedValue": u"Standard DAv4 Family vCPUs", u"value": u"standardDAv4Family"}, u"unit": u"Count"}, {u"currentValue": 0, u"limit": 0, u"name": {u"localizedValue": u"Standard DASv4 Family vCPUs", u"value": u"standardDASv4Family"}, u"unit": u"Count"}, {u"currentValue": 0, u"limit": 0, u"name": {u"localizedValue": u"Standard EAv4 Family vCPUs", u"value": u"standardEAv4Family"}, u"unit": u"Count"}, {u"currentValue": 0, u"limit": 0, u"name": {u"localizedValue": u"Standard EASv4 Family vCPUs", u"value": u"standardEASv4Family"}, u"unit": u"Count"}, {u"currentValue": 0, u"limit": 0, u"name": {u"localizedValue": u"Standard NDSv3 Family vCPUs", u"value": u"standardNDSv3Family"}, u"unit": u"Count"}, {u"currentValue": 0, u"limit": 8, u"name": {u"localizedValue": u"Standard DCSv2 Family vCPUs", u"value": u"standardDCSv2Family"}, u"unit": u"Count"}, {u"currentValue": 0, u"limit": 0, u"name": {u"localizedValue": u"Standard NVSv4 Family vCPUs", u"value": u"standardNVSv4Family"}, u"unit": u"Count"}, {u"currentValue": 0, u"limit": 0, u"name": {u"localizedValue": u"Standard NDSv2 Family vCPUs", u"value": u"standardNDSv2Family"}, u"unit": u"Count"}, {u"currentValue": 0, u"limit": 0, u"name": {u"localizedValue": u"Standard NPS Family vCPUs", u"value": u"standardNPSFamily"}, u"unit": u"Count"}, {u"currentValue": 0, u"limit": 0, u"name": {u"localizedValue": u"Standard HBrsv2 Family vCPUs", u"value": u"standardHBrsv2Family"}, u"unit": u"Count"}, {u"currentValue": 0, u"limit": 50000, u"name": {u"localizedValue": u"Standard Storage Managed Disks", u"value": u"StandardDiskCount"}, u"unit": u"Count"}, {u"currentValue": 0, u"limit": 50000, u"name": {u"localizedValue": u"Premium Storage Managed Disks", u"value": u"PremiumDiskCount"}, u"unit": u"Count"}, {u"currentValue": 0, u"limit": 50000, u"name": {u"localizedValue": u"StandardSSDStorageDisks", u"value": u"StandardSSDDiskCount"}, u"unit": u"Count"}, {u"currentValue": 0, u"limit": 1000, u"name": {u"localizedValue": u"UltraSSDStorageDisks", u"value": u"UltraSSDDiskCount"}, u"unit": u"Count"}, {u"currentValue": 0, u"limit": 50000, u"name": {u"localizedValue": u"StandardStorageSnapshots", u"value": u"StandardSnapshotCount"}, u"unit": u"Count"}, {u"currentValue": 0, u"limit": 50000, u"name": {u"localizedValue": u"PremiumStorageSnapshots", u"value": u"PremiumSnapshotCount"}, u"unit": u"Count"}, {u"currentValue": 0, u"limit": 50000, u"name": {u"localizedValue": u"ZrsStorageSnapshots", u"value": u"ZRSSnapshotCount"}, u"unit": u"Count"}, {u"currentValue": 0, u"limit": 16384, u"name": {u"localizedValue": u"UltraSSDTotalSizeInGB", u"value": u"UltraSSDDiskSizeInGB"}, u"unit": u"Count"}]})

VMSSPROPERTIES_DEMO = json.dumps([u"dashdemo", 1, u"brazilsouth", u"dashdemo", u"UbuntuServer", u"16.04.0-LTS", u"Succeeded", u"dashdemo.brazilsouth.cloudapp.azure.com", u"999.999.999.999"])

VMSSVMS_DEMO = json.dumps({"value": [{u"sku": {u"tier": u"Standard", u"name": u"Standard_A2"}, u"name": u"dashdemo_0", u"instanceId": u"0", u"properties": {u"osProfile": {u"adminUsername": u"blackpanther", u"secrets": [], u"computerName": u"dashdemo000000", u"linuxConfiguration": {u"disablePasswordAuthentication": False}}, u"networkProfile": {u"networkInterfaces": [{u"id": u"/subscriptions/99999999-aaaa-bbbb-cccc-888888888888/resourceGroups/dashdemo/providers/Microsoft.Compute/virtualMachineScaleSets/dashdemo/virtualMachines/0/networkInterfaces/dashdemonic"}]}, u"storageProfile": {u"imageReference": {u"sku": u"16.04.0-LTS", u"publisher": u"Canonical", u"version": u"16.04.201903130", u"offer": u"UbuntuServer"}, u"osDisk": {u"osType": u"Linux", u"vhd": {u"uri": u"https://ababababababcdashdemosa.blob.core.windows.net/dashdemovhd/dashdemoosdisk-os-0-1111111111111111111111111111111.vhd"}, u"createOption": u"FromImage", u"name": u"dashdemoosdisk-os-0-11111111111111111111111111111111", u"caching": u"ReadOnly"}}, u"vmId": u"22222222-oooo-uuuu-hhhh-333333333333", u"hardwareProfile": {}, u"latestModelApplied": False, u"provisioningState": u"Succeeded"}, u"location": u"brazilsouth", u"type": u"Microsoft.Compute/virtualMachineScaleSets/virtualMachines", u"id": u"/subscriptions/99999999-aaaa-bbbb-cccc-888888888888/resourceGroups/dashdemo/providers/Microsoft.Compute/virtualMachineScaleSets/dashdemo/virtualMachines/0"}]})

VMDETAILS_DEMO = json.dumps({u"computerName": u"dashdemo000000", u"disks": [{u"name": u"dashdemoosdisk-os-0-11111111112222222222333333333344", u"statuses": [{u"time": u"2019-05-03T20:46:26.6712371+00:00", u"code": u"ProvisioningState/succeeded", u"displayStatus": u"Provisioning succeeded", u"level": u"Info"}]}], u"osName": u"ubuntu", u"platformUpdateDomain": 0, u"vmAgent": {u"vmAgentVersion": u"2.2.46", u"extensionHandlers": [], u"statuses": [{u"time": u"2020-03-18T23:03:37+00:00", u"message": u"Guest Agent is running", u"code": u"ProvisioningState/succeeded", u"displayStatus": u"Ready", u"level": u"Info"}]}, u"platformFaultDomain": 0, u"placementGroupId": u"88888888-4444-4444-4444-121212121212", u"osVersion": u"16.04", u"statuses": [{u"time": u"2019-05-03T20:47:37.2369051+00:00", u"code": u"ProvisioningState/succeeded", u"displayStatus": u"Provisioning succeeded", u"level": u"Info"}, {u"code": u"PowerState/running", u"displayStatus": u"VM running", u"level": u"Info"}]})

VMNIC_DEMO = json.dumps({u"value": [{u"properties": {u"provisioningState": u"Succeeded", u"macAddress": u"00-00-00-00-00-00", u"virtualMachine": {u"id": u"/subscriptions/88888888-4444-4444-4444-121212121212/resourceGroups/vmssdash/providers/Microsoft.Compute/virtualMachineScaleSets/vmssdash/virtualMachines/0"}, u"dnsSettings": {u"internalDomainNameSuffix": u"11111111111111111111111111.nx.internal.cloudapp.net", u"dnsServers": [], u"appliedDnsServers": []}, u"primary": True, u"resourceGuid": u"88888888-4444-4444-4444-121212121212", u"enableIPForwarding": False, u"ipConfigurations": [{u"properties": {u"subnet": {u"id": u"/subscriptions/88888888-4444-4444-4444-121212121212/resourceGroups/DASHDEMO/providers/Microsoft.Network/virtualNetworks/vmssdashvnet/subnets/dashdemosubnet"}, u"primary": True, u"privateIPAddressVersion": u"IPv4", u"privateIPAllocationMethod": u"Dynamic", u"privateIPAddress": u"10.0.0.5", u"provisioningState": u"Succeeded"}, u"etag": u"W/\'88888888-4444-4444-4444-121212121212\'", u"name": u"dashdemoipconfig", u"id": u"/subscriptions/88888888-4444-4444-4444-121212121212/resourceGroups/DASHDEMO/providers/Microsoft.Compute/virtualMachineScaleSets/dashdemo/virtualMachines/0/networkInterfaces/dashdemonic/ipConfigurations/dashdemoipconfig"}], u"enableAcceleratedNetworking": False}, u"etag": u"W/\'88888888-4444-4444-4444-121212121212\'", u"name": u"dashdemonic", u"id": u"/subscriptions/88888888-4444-4444-4444-121212121212/resourceGroups/DASHDEMO/providers/Microsoft.Compute/virtualMachineScaleSets/dashdemo/virtualMachines/0/networkInterfaces/dashdemonic"}]})