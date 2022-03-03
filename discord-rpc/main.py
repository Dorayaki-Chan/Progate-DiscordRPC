import rpc
import time
from time import mktime

import test

import settings

client_id = settings.client_id

print("Demo for python-discord-rpc Adobe illustrator")
#client_id = '942579429215965224'  # Your application's client ID as a string. (This isn't a real client ID)
rpc_obj = rpc.DiscordIpcClient.for_platform(client_id)  # Send the client ID to the rpc module
print("RPC connection successful.")

time.sleep(5)
start_time = mktime(time.localtime())
while True:
    sstring = test.chromeURL()
    activity = {
            "state": "脱線よくします",  # anything you like
            "details": sstring,  # anything you like
            "timestamps": {
                "start": start_time
            },
            "assets": {
                "small_text": "Operation by Progate",  # anything you like
                "small_image": "progate",  # must match the image key
                "large_text": "Progate",  # anything you like
                "large_image": "app"  # must match the image key
            },
            "buttons" : [{"label" : "PROGATE", "url" : "https://prog-8.com/"}]
        }
    rpc_obj.set_activity(activity)
    time.sleep(30)
