#!/bin/bash
# This script sends a JSON POST request to a URL with the contents of a file in the body of the request, and displays the body of the response.

# Check if the user has provided both URL and file arguments
if [ $# -ne 2 ]; then
    echo "Usage: $0 <URL> <file>"
    exit 1
fi

# Store the URL and file provided by the user
url=$1
file=$2

# Check if the file exists
if [ ! -f "$file" ]; then
    echo "Error: File '$file' not found"
    exit 1
fi

# Send a POST request with the contents of the file in the body and store the response body
response=$(curl -s -X POST -H "Content-Type: application/json" -d "@$file" $url)

# Display the body of the response
echo "$response"
