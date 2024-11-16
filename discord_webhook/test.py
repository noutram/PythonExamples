print("Webhook test")

# Post "Hello Luca" to the webhook  https://discord.com/api/webhooks/1307347990628925461/7xnzn7Xdwe8fznUKvQAQLmT9F6p1dFinIWUfMMR-gre3BU90Zwn_ggwdueLBfkCxroQc

import requests
import json

# Webhook URL
url = "https://discord.com/api/webhooks/1307347990628925461/7xnzn7Xdwe8fznUKvQAQLmT9F6p1dFinIWUfMMR-gre3BU90Zwn_ggwdueLBfkCxroQc"

embed = {
    "title": "Submessage",
    "description": "This is an embedded message",
    "color": 0x00FF00
}

# Message to send
message = {
    "content": "Hello **Luca**, your new highscore is -1\n😂",
    "embeds": [embed]
}

# Send the message
response = requests.post(url, json=message)

