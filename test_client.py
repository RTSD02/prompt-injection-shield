# Pretends to be a client's chatbot that calls your Shield API.
import requests

url = input("Paste your API address (example: https://prompt-shield-api.onrender.com): ").strip().rstrip("/")
key = input("Paste your API key: ").strip()

print("\nType a message and press Enter. Type quit to stop.\n")
while True:
    msg = input("Customer: ")
    if msg.strip().lower() == "quit":
        break
    try:
        r = requests.post(
            url + "/check",
            json={"text": msg},
            headers={"x-api-key": key},
            timeout=90,
        )
        if r.status_code != 200:
            print("Error:", r.status_code, r.text, "\n")
            continue
        data = r.json()
        if data["is_attack"]:
            print(f"Chatbot: Sorry, I can't help with that.  [BLOCKED, score {data['score']}]\n")
        else:
            print(f"Chatbot: (message passed to the chatbot)  [ALLOWED, score {data['score']}]\n")
    except Exception as e:
        print("Could not reach the API:", e, "\n")
