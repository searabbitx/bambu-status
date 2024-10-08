# Bambu status

## Api key
To specify the api key, use the `api_key` secret in docker. If you use the `docker-compose.yml` file provided with the repo, create the `api_key.txt` file with your key.

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
  127.0.0.1:5000/bambu_status
```

