from flask import Flask, request, make_response,render_template
import json, serial

###########
# 執行前先將 ServoControlArduino 程式上傳後
# 打開 Arduino 電源
###########

app = Flask(__name__)
ser = serial.Serial('/dev/ttyACM0',115200,timeout=1)

@app.route('/test', methods=['POST'])
def index():
    carCmd = {'f':'forward\n','l':'left\n','r':'right\n','b':'back\n','s':'stop\n'}
    returnText = {'f':'前進','l':'左轉','r':'右轉','b':'後退','s':'停止'} 
    data = request.form['message']
    if data in carCmd:
        ser.write(carCmd[data].encode())
        return '目前行進方向:' + returnText[data]
    return '???'

@app.route('/')
def main():
    return render_template('index.html')
    
if __name__ == "__main__":
    app.run(host="127.0.0.1")
    