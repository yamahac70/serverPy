# boot.py -- run on boot-up
import network

#const char* ssid = "Arlab_5930";
#const char* password = "9263
SSID  = 'Arlab_5930'
SSI_PASSWORD  = '92637139'


def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(SSID, SSI_PASSWORD)
        while not sta_if.isconnected():
            pass
    print('Connected! Network config:', sta_if.ifconfig())
    
print("Connecting to your wifi...")
do_connect()