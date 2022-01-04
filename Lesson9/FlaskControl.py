from flask import Flask, render_template
# import RPi.GPIO as GPIO

app = Flask(__name__)

# GPIO.setmode(GPIO.BCM)
# GPIO.setup(14, GPIO.OUT)
# GPIO.output(14, GPIO.LOW)

@app.route("/")
def index():
    # GPIO.output(14, GPIO.LOW)
    return render_template('hyperlink.html')

@app.route("/on")
def LED_On():
    # GPIO.output(14, GPIO.HIGH)
    return render_template('hyperlink.html')

@app.route("/off")
def LED_Off():
    # GPIO.output(14, GPIO.LOW)
    return render_template('hyperlink.html')

if __name__ == "__main__":
    app.run(host='127.0.0.1')
