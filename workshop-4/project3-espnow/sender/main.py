import network
import espnow

# A WLAN interface must be active to send()/recv()
sta = network.WLAN(network.STA_IF)  # Or network.AP_IF
sta.active(True)
mac = sta.config('mac')
print(mac)
sta.disconnect()      # For ESP8266

e = espnow.ESPNow()
e.active(True)

# MAC address of peer's wifi interface
peer = b'\xc8\xf0\x9e\x9f}\x88'   

e.add_peer(peer)      # Must add_peer() before send()

e.send(peer, "Starting...")
for i in range(100):
    e.send(peer, str(i)*20, True)
e.send(peer, b'end')