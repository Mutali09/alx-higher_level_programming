#!/bin/bash
# This script sends a DELETE request to the URL passed as the first argument and displays the body of the response.

# Check if the user has provided a URL as an argument
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Store the URL provided by the user
url=$1

# Send a DELETE request to the URL and store the response body
response=$(curl -s -X DELETE $url)

# Display the body of the response
echo "$response"
