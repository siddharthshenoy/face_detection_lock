#!/bin/bash

API="o.UuJMCpaKR6j5xn5w0A1hmxgQbeAHlka2"
MSG="$1"

curl -u $API: https://api.pushbullet.com/v2/pushes -d type=note -d title="Alert" -d body="$MSG"