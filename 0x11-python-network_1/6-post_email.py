#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    # Assuming the script takes URL and email as command-line arguments
    url = sys.argv[1]
    email = sys.argv[2]

    # Data to be sent in the POST request
    data = {'email': email}

    try:
        # Send POST request using requests
        response = requests.post(url, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors (e.g., 404, 500)

        # Display the body of the response
        print("Response Body:")
        print(response.text)
    except requests.exceptions.RequestException as e:
        print("Error occurred:", e)

