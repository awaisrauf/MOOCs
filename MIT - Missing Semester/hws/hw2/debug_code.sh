#!/bin/bash
./debug_script.sh
count=0
one=1
while [ $? -eq 0 ]; do
count=$((count + 1))
./debug_script.sh
done
echo "done and cunt= $count"
