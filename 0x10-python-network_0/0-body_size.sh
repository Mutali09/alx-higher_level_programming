#!/bin/bash

# This script sends a request to a given URL using curl and displays the size of the response body in bytes.

# Check if a URL argument is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Get the URL from the command line argument
url="$1"

# Send a request using curl and store the response in a temporary file
response_file=$(mktemp)
curl -s "$url" > "$response_file"

# Calculate the size of the response body in bytes
response_size=$(wc -c < "$response_file")

# Display the size
echo "Size of the response body: $response_size bytes"

# Clean up the temporary file
rm "$response_file"
