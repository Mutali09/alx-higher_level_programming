#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    # Assuming the script takes the URL as a command-line argument
    url = sys.argv[1]

    try:
        response = requests.get(url)
        status_code = response.status_code
        
        if status_code >= 400:
            print("Error code:", status_code)
        else:
            print(response.text)
    except requests.exceptions.RequestException as e:
        print("Error occurred:", e)
