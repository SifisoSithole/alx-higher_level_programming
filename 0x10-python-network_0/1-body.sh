#!/bin/bash
# script that takes in a URL, sends a request to that URL, and displays the size of the body of the response

ST=$(curl -Is "$1" | head -1 | cut -d ' ' -f2)
if [[ $ST -eq 200 ]]
then
	curl -sX  GET "$1"
fi
