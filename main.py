from microdot import Microdot, Response
from microdot_utemplate import render_template
from machine import Pin
from time import sleep
led = Pin(2, Pin.OUT)

app = Microdot()
Response.default_content_type = 'text/html'

@app.route('/')
def index(request):
    return render_template('index.html', ledValor=0)

@app.route('/orders', methods=['GET'])
def index(req):
    name = "donsky"
    orders = ["soap", "shampoo", "powder"]

    return render_template('orders.html', name=name, orders=orders)
@app.route('/ledOn', methods=['GET'])
def led_on(req):
    led.value(1)
    return render_template('index.html', ledValor=1)
@app.route('/ledOff', methods=['GET'])
def led_on(req):
    led.value(0)
    return render_template('index.html', ledValor=0)
@app.route('/ledToggle', methods=['GET'])
def led_toggle(req):
    led.value(not led.value())
    return render_template('index.html', ledValor=led.value())

@app.route('/num', methods=['GET'])
async def generate_fibonacci(req):
        i=10
        for i in range(10):
            yield str(i) + '\n'

        return generate_fibonacci()
        


if __name__ == '__main__':
    app.run(debug=True)