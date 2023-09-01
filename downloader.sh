#!/bin/bash

# Read each line from links.txt and execute the exercism download command
while IFS= read -r exercise; do
    if [ -n "$exercise" ]; then
        exercism download --exercise="$exercise" --track=rust
    fi
done < links.txt

