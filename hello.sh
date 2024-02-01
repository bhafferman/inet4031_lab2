#!/bin/bash
              
              a=2
              b=2
              c=$((a + b))
              
              echo "Bash says: Hello, World!"
              echo "$a + $b = $c"
user_array=("User1" "User2" "User2")

# Printing the array
# echo "${user_array[@]}"
for user in "${user_array[@]}"; do
    echo "$user"
done
