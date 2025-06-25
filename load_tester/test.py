import threading
import requests

def send_request():
    try:
        response = requests.post("http://localhost:5000/request_charge")
        print(response.status_code, response.json())
    except Exception as e:
        print("Error:", e)

threads = []
for _ in range(100):  # Simulate 100 EVs
    t = threading.Thread(target=send_request)
    t.start()
    threads.append(t)

for t in threads:
    t.join()
