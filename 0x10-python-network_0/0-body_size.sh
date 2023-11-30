#!/bin/bash
# Bash script that takes in a URL, sends a request to that URL,
# and displays the size of the body of the response
# The size must be displayed in bytes


url=$1

# Use curl to send a request and store the response in a variable
response=$(curl -sI "$url")

# Extract the Content-Length from the response headers
content_length=$(echo "$response" | grep -iE '^Content-Length:' | awk '{print $2}' | tr -d '\r\n')

echo "$content_length"
