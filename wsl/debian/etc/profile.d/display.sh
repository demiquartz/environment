export DISPLAY=$(ip route | grep 'default via' | awk '{print $3}'):0
