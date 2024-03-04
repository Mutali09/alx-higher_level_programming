#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    # Assuming the script takes the URL as a command-line argument
    url = sys.argv[1]

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors (e.g., 404, 500)

        x_request_id = response.headers.get('X-Request-Id')
        if x_request_id:
            print("Value of X-Request-Id:", x_request_id)
        else:
            print("X-Request-Id not found in the response header.")
    except requests.exceptions.RequestException as e:
        print("Error occurred:", e)
