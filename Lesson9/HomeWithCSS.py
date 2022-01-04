from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def index():
    text = request.args.get('username')
    if text == None: text = "User"
    return render_template('home.html', user_template=text)
    
if __name__ == '__main__':
    app.run(host='127.0.0.1')
