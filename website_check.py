import requests

url = "https://mysmsfproperty.com.au"

try:
    response = requests.get(url)
    if response.status_code == 200:
        print(f" Success! {url} is UP.")
    else:
        print(f"️ Warning! {url} returned status: {response.status_code}")
except Exception as e:
    print(f" Error: Could not connect to {url}. Details: {e}")

