#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    # Get the letter from command-line arguments or set it to an empty string if not provided
    q = sys.argv[1] if len(sys.argv) > 1 else ""

    # Data to be sent in the POST request
    data = {'q': q}

    try:
        # Send POST request using requests
        response = requests.post("http://0.0.0.0:5000/search_user", data=data)
        response_json = response.json()  # Parse the JSON response

        if response_json:  # Check if the JSON response is not empty
            if 'id' in response_json and 'name' in response_json:
                print("[{}] {}".format(response_json['id'], response_json['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
    except requests.exceptions.RequestException as e:
        print("Error occurred:", e)

