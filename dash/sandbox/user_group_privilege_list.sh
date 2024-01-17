#!/bin/bash

while IFS=: read -r user _ uid gid _ _ _; do
    # Check if UID is a number and greater than or equal to 500
    if [[ "$uid" =~ ^[0-9]+$ ]] && [ "$uid" -ge 100 ]; then
        group=$(awk -F: -v gid="$gid" '$3 == gid { print $1 }' /etc/group)
        echo "User: $user, Group: $group"
    fi
done < /etc/passwd

