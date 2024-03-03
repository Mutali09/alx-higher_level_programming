#!/bin/bash
# This script takes a URL as an argument, sends a POST request to the URL with specified parameters, and displays the body of the response.

# Check if the user has provided a URL as an argument
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Store the URL provided by the user
url=$1

# Define the POST parameters
email="test@gmail.com"
subject="I will always be here for PLD"

# Send a POST request to the URL with the specified parameters and store the response body
response=$(curl -s -X POST -d "email=$email" -d "subject=$subject" $url)

# Display the body of the response
echo "$response"
