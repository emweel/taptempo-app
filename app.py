from flask import Flask, render_template, request, session, jsonify
import time
import functools

app = Flask(__name__)
app.config['SECRET_KEY'] = 'devkey'

def add_delta(x, y):
    return float(x) + float(y)

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'timelist' not in session:
        session['timelist'] = []
    
    if request.method == 'POST':
        if 'last_time' not in session:
            session['last_time'] = time.time()
            return jsonify({"tempo": "--"})

        curr_time = time.time()
        t_delta = curr_time - session['last_time']
        session['last_time'] = curr_time

        if len(session['timelist']) > 3:
            session['timelist'].pop(0)

        session['timelist'].append(t_delta)
        session.modified = True

        avg_delta = functools.reduce(add_delta, session['timelist'])
        tempo = 1 * 60 / (avg_delta / len(session['timelist']))

        return jsonify({"tempo": format(tempo, '.2f')})

    return render_template('index.html', curTempo = '--')

if __name__ == '__main__':
    app.run()
