from flask import Flask, render_template, request, redirect, session
import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "BigBrews-23",
    auth_plugin="mysql_native_password",
    database = "episteme_db"
)

app = Flask(__name__, static_folder='static')
app.secret_key = 'BigBrews-23'

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

'''
THESIS SUBMISSION SQL
THESIS SUBMISSION SQL
THESIS SUBMISSION SQL
'''

@app.route('/submit_form', methods=['POST'])
def submit_form():
    # Get the form data
    thesis_title = request.form['thesis_title']
    group_name = request.form['group_name']
    professor_name = request.form['professor_name']
    abstract = request.form['abstract']
    school = request.form['school']
    
    # Retrieve other form fields as needed

    # dbect to the MySQL database
    cursor = db.cursor()

    # Insert the data into the database
    query = "INSERT INTO thesis (thesis_title, group_name, professor_name, abstract, school) VALUES (%s, %s, %s, %s, %s)"
    values = (thesis_title, group_name, professor_name, abstract, school)
    cursor.execute(query, values)
    db.commit()

    # Close the database dbection
    cursor.close()
    db.close()

    return 'Data inserted successfully.'

'''
REGISTRATION TO SQL
REGISTRATION TO SQL
REGISTRATION TO SQL
'''
@app.route('/register_py', methods=['POST'])
def register_py():
    # Get the form data
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email_address = request.form['email_address']
    password = request.form['password']
    
    # Retrieve other form fields as needed

    # dbect to the MySQL database
    cursor = db.cursor()

    # Insert the data into the database
    query = "INSERT INTO user (first_name, last_name, email_address, password) VALUES (%s, %s, %s, %s)"
    values = (first_name, last_name, email_address, password)
    cursor.execute(query, values)
    db.commit()

    # Close the database dbection
    cursor.close()
    db.close()

    return 'Data inserted successfully.'

'''
SELECTION TABLE
SELECTION TABLE
SELECTION TABLE
'''

@app.route('/login_py', methods=['POST'])
def login():
    email_address = request.form['email_address']
    password = request.form['password']

    cursor = db.cursor()
    cursor.execute("SELECT * FROM user WHERE email_address = %s AND password = %s", (email_address, password))
    user = cursor.fetchone()

    if user:
        session['email_address'] = user[1]  # Assuming the email_address column is in index 1
        return redirect('/selection')
    else:
        return 'Invalid email/password combination'



if __name__ == '__main__':
    app.run(debug=True)
