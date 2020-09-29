from wifi_lib import conecta
import urequests
import dht
import machine
import time

d = dht.DHT11(machine.Pin(4))
r = machine.Pin(2, machine.Pin.OUT)

station = conecta("NOME_SUA_REDE", "SUA_SENHA")

if station.isconnected():
   print("Conectado")

while True:
    d.measure()
    print("Temp={} Umid={}".format(d.temperature(), d.humidity()))
    

    if d.temperature() >=31 or d.humidity() >=70:
       r.value(1)
       siteAcessado = urequests.get("http://api.thingspeak.com/update?api_key=CHAVEDOTHINKSPEAK&field1={}&field2={}".format(d.temperature(),d.humidity()))
       print(siteAcessado.text)
       print("Envio concluído")
    
    else:
       print("Condições mínimas não alcançadas")
       r.value(0)
    time.sleep(20)
