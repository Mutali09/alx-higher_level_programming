#!/usr/bin/python3
import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors (e.g., 404, 500)
        
        print("- Body response:")
        print("\t- type:", type(response.text))
        print("\t- content:", response.text)
    except requests.exceptions.RequestException as e:
        print("Error occurred:", e)

