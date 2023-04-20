


import network
ap_if = network.WLAN(network.AP_IF)
ap_if.active(True)

ap_if.config(essid="Bass",password="bc20cf7f5c5e")
ap_if.config(channel=11,authmode=network.AUTH_WPA2_PSK)



