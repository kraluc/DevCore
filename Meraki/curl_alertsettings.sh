curl -C PUT \
  --url https://api.meraki.com/api/v0/networks/networkId4/alertSettings \
  -H 'X-Cisco-Meraki-API-Key: 877ca5b25d45eb0dd434468112eb267b79a6dcaa' \
  -H  'Accept: application/json' \
  -H 'Content-Type: application/json' \
  --data-raw ' {
    "defaultDestinations": {
        "emails": [
            "miles@meraki.com"
        ],
        "allAdmins": true,
        "snmp": true,
    },
    "alerts": [
        {
            "type": "gatewayDown",
            "enabled": true,
            "alertsDestination": {
                "emails": [
                    "miles@meraki.com"
                ],
                "allAdmins": false,
                "snmp": false,
            },
            "filters": {
                "timeout": 60
            }
        }
    ]
}'