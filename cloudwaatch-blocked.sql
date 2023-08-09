fields @timestamp, httpRequest.clientIp
| filter action = 'BLOCK'
| sort @timestamp desc
| limit 20
