import requests
import json

url = "https://www.hotels.com/ho117116/millennium-hotel-london-knightsbridge-london-united-kingdom/?chkin=2022-10-19&chkout=2022-10-20&x_pwa=1&rfrr=HSR&pwa_ts=1664987377392&referrerUrl=aHR0cHM6Ly93d3cuaG90ZWxzLmNvbS9Ib3RlbC1TZWFyY2g%3D&useRewards=false&rm1=a2&regionId=2114&destination=London%2C+England%2C+United+Kingdom&destType=MARKET&neighborhoodId=553248635976382803&trackingData=AAAAEIUEIIpTiidNfsuiataGXyyK2nSRpI5AAnYlwHkqHFbApK90-ulxOQuHZb_0w3ULx49HEd3kp3jcuC0OGZJvRI2zCYNp2cH3RxcS1RIImK0OWPrKl33DtlayIplWfgRotg7vgidMUHitDVQC4D9D7TqL5pggvHqkMg36BNlkGGh0VuBCFZSZvKoCsmz0acVgvuAaIaCz5piCbXPRko8_nYPgeyhfeCYK7qAkiCtZh5FD2PPnFCjPOIbxXCypA7UIcAH_98klf2Gvg69Of7MJ6VX6njFkY6tXve8ezPeLbUC3Z6QO6juQN91mD_kvmmumWQPP_vRFUwBlBecN5qzoDkwvBcsP_R_yD89oxFafCIDEyQS26Aksl-ZkWsD9K0_3YktpyzU2CjVVHSd-LUDXYoI-crjWfl6czoHv_SuQbmhzikLYGZDFX8f-lAhlIUVPKeYfqSi0_4mvayhhKdaVTwdz2Kq9L6iIsY9MevjpahHtsKNQBumR2gPyG7OmLzXcuWE2iR0ODDZi4eXmTBibjcxAabKKcJw5QHfa4zuru54QsncOpreCviBSWha_xQHz_h0zNVQNDr6ZPpcn9ogV__0U0kYOi0BvledcxfJPd3aKTAw4lSS0PV5wV4TeF51LVEglkclvOGhmXrijyC9UJQxeEXOkJaXgc3u_GW4TFmuMYJBWepIpMGhkoYia-TiUDhbThI0TQkEGJIhyDMSejJjClED7K_ejV99r4ML_qM-jOnnHoTZNvJuXvi9fTxiEue7CRSPBxkACQeBjysn86yCaTzDjjyigK6mdg0sXoEfv2VBOtrNDhLIYDXv3_IK1VTX43VzxWF-c3ikWNUvE4PK3JNOfGqMLGzE0E2QmRZkhHXcrjaWEL6kVIrSR7Ns0MzFqXE16TLCpX-oUjoAP8Xj_NJwNQXpR_6yKf8plhxB7XULedMcLrnMG2X6bVbtLTYdirWSOP7lyZWwFGmq9GdbjehafsFnpLnh1jTPp2mI4xk0_2eT_RNe2LDBTpOE14A%3D%3D&rank=1&testVersionOverride=Buttercup%2C44204.0.0%2C44203.0.0%2C43549.129874.3%2C43550.131256.0%2C31936.102311.0%2C33775.98848.1%2C38414.114301.0%2C39483.0.0%2C38427.115718.1%2C42444.0.0%2C42589.0.0%2C42876.124673.0%2C42973.0.0%2C42974.0.0%2C42975.0.0%2C42976.0.0%2C42802.125960.1%2C33739.99567.0%2C37898.109354.0%2C37930.0.0%2C37949.0.0%2C37354.0.0%2C43435.128144.0%2C44700.131646.0%2C44704.0.0&slots=HSR_A&position=1&beaconIssued=2022-10-05T16%3A29%3A36&sort=RECOMMENDED&top_dp=379&top_cur=EUR&semdtl=&userIntent=&selectedRoomType=200048296&selectedRatePlan=266157351&expediaPropertyId=5813"

headers = {
	"X-RapidAPI-Key": "9adf9fc99fmsh6713e606247ad93p17623ejsn60318b0a84af",
	"X-RapidAPI-Host": "hotels4.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

# print(response.text)
data = json.loads(response.text)
# print(data)
with open('hotels.json', 'w') as file:
	json.dump(data, file, indent=4)

