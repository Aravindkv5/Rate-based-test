fields @timestamp, httpRequest.clientIp, action
| filter action = 'BLOCK'
| sort @timestamp desc
| limit 20 
