# Bambu status

## Api key
To specify the api key, use the `api_key` secret in docker

## Status update endpoint

Example curl call to the status update endpoint:

```bash
curl -v -X PUT -H 'Content-Type: application/json' \
  -H 'X-Api-Key: <YOUR_API_KEY>' \
  --data '
{
  "amsHumidity": "1",
  "amsTemp": "32.5",
  "bedTargetTemper": "40",
  "bedTemper": "40",
  "chamberTemper": "34",
  "failReason": "0",
  "gcodeState": "RUNNING",
  "mcPercent": "78",
  "mcPrintErrorCode": "0",
  "mcRemainingTime": "1337",
  "nozzleTargetTemper": "1337",
  "nozzleTemper": "1337",
  "printError": "0",
  "subtask_name": "Test data update..."
}
' \
  192.168.122.239:5000/bambu_status
```

