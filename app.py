from flask import Flask, render_template

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/log_in')
def log_in():
    return render_template('logged_out/log_in.html')

@app.route('/register')
def register():
    return render_template('logged_out/register.html')

if __name__ == '__main__':
    app.run(debug=True)