from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/hello')
def hello():
    return 'Hello stinkin world!'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return render_template('index.html', curTempo= '1')

    return render_template('index.html', curTempo = '0')

if __name__ == '__main__':
    app.run()
