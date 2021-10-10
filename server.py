from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route("/")
def my_homr():
    return render_template('index.html')


@app.route('/<string:page_name>')
def get_page(page_name=None):
    return render_template(page_name)

'''

we originally had thing, now we'll make it dynamic
@app.route("/index.html")
def my_home():
    return render_template('index.html')

@app.route('/about.html')
def my_aboutMe():
    return render_template('about.html')

@app.route('/work.html')
def my_work():
    return render_template('work.html')

@app.route('/works.html')
def my_works():
    return render_template('works.html')

@app.route('/contact.html')
def my_contact():
    return render_template('contact.html')

now we'll make the Contact page work

we want a func which will write to our database.txt

def write_to_db(data):
    with open('database.txt', mode='a') as database:
        # data is the dict of email, subject, object from the submit
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f' email, sub, mes')
        # creates a new line for each submit

now we want to write to a csv file 

'''

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        # data is the dict of email, subject, object from the submit
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n {email}, {subject}, {message}')
        # creates a new line for each submit

def write_to_csv(data):
    with open('db.csv', newline='', mode='a') as db:
        # data is the dict of email, subject, object from the submit
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(db, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

@app.route('/submit_form', methods=['POST', 'GET']) # creating a route for the submitting of a form
def submit_form():
    if request.method == 'POST':
        # if the method used was a post request
        data = request.form.to.dict()
        write_to_file(data)
        # changes form data to dictionary
        return redirect('thankyou.html')
