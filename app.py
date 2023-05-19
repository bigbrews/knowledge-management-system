from flask import Flask, render_template

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

# Accounts route

@app.route('/log_in')
def log_in():
    return render_template('logged_out/log_in.html')

@app.route('/register')
def register():
    return render_template('logged_out/register.html')

# Selections route

@app.route('/selection')
def selection():
    return render_template('logged_in/selection/selection.html')

@app.route('/submission_form')
def submission_form():
    return render_template('logged_in/homepage/submission_form.html')

@app.route('/knowledge_library')
def knowledge_library():
    return render_template('logged_in/homepage/knowledge_library.html')

# Admins route

@app.route('/admin')
def admin():
    return render_template('logged_in/admin/admin.html')

if __name__ == '__main__':
    app.run(debug=True)
