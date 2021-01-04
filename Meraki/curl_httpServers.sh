 curl -C PUT \
  --url https://api.meraki.com/api/v0/networks/networkId4/ \
  -H 'X-Cisco-Meraki-API-Key: 877ca5b25d45eb0dd434468112eb267b79a6dcaa' \
  -H  'Accept: application/json' \
  -H 'Content-Type: application/json' \
  --data-raw ' {
     "name": "My HTTP Server",
     "url": "https://www.example.com/webhooks",
     "sharedSecret": "foobar",
 }'