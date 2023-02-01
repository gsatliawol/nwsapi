#!/bin/bash
read time temp <<< $(curl -s "https://api.weather.gov/stations/KBFI/observations/latest" | jq '.properties.timestamp, .properties.temperature.value')
echo "Time is: " $time
echo "Temp is: " $temp
