from flask import Flask, render_template, request, session
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'devkey'

@app.route('/hello')
def hello():
    return 'Hello stinkin world!'

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'timelist' not in session:
        session['timelist'] = 0
    
    if request.method == 'POST':
        if 'last_time' not in session:
            session['last_time'] = time.time()
            return render_template('index.html', curTempo = '--')

        session['last_time'] = session['timelist']
        session['timelist'] = time.time()
        #tempo = str(session['timelist']) + ' ' + str(session['last_time'])
        tempo = 1 * 60 / (session['timelist'] - session['last_time'])

        return render_template('index.html', curTempo= format(tempo, '.0f'))

    return render_template('index.html', curTempo = '--')

if __name__ == '__main__':
    app.run()
