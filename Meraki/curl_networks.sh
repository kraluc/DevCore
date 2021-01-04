curl --request GET \
-L --url https://api.meraki.com/api/v0/organizations/739153288842183267/networks \
--header 'X-Cisco-Meraki-API-Key: 877ca5b25d45eb0dd434468112eb267b79a6dcaa' | python -m json.tool
#   % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
#                                  Dload  Upload   Total   Spent    Left  Speed
# 100   138    0   138    0     0    439      0 --:--:-- --:--:-- --:--:--   438
# 100   297    0   297    0     0    181      0 --:--:--  0:00:01 --:--:--     0
# [
#     {
#         "disableMyMerakiCom": false,
#         "disableRemoteStatusPage": true,
#         "id": "L_739153288842208045",
#         "name": "Layann salame",
#         "organizationId": "739153288842183267",
#         "productTypes": [
#             "appliance",
#             "cellular gateway",
#             "environmental",
#             "switch",
#             "wireless"
#         ],
#         "tags": null,
#         "timeZone": "America/Los_Angeles",
#         "type": "combined"
#     }
# ]