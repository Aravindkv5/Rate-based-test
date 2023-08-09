import requests
import time

url = "https://managed-update.cloudin.social"
total_requests = 150
time_limit = 300  # 5 minutes in seconds

start_time = time.time()
requests_sent = 0

while requests_sent < total_requests:
    response = requests.get(url)
    requests_sent += 1
    print(f"Request {requests_sent} - Status Code: {response.status_code}")

    elapsed_time = time.time() - start_time
    if elapsed_time > time_limit:
        break

    time.sleep(1)  # Wait for 1 second between requests

print("Finished sending requests.")
