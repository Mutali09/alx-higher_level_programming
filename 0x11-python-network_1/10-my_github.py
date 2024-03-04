#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    # Assuming the script takes GitHub username and personal access token as command-line arguments
    username = "Mutali09"
    password = "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"

    # URL for the GitHub API to get user information
    url = f"https://api.github.com/user"

    try:
        # Send GET request to the GitHub API with Basic Authentication
        response = requests.get(url, auth=(username, password))

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            user_info = response.json()
            # Display the user's id
            print("Your GitHub user id:", user_info["id"])
        else:
            print("Error:", response.status_code)
    except requests.exceptions.RequestException as e:
        print("Error occurred:", e)
