from flask import Flask, render_template, request, redirect
import csv


app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route("/contact.html")
def contact():
    return render_template('contact.html')


@app.route("/thankyou.html")
def thankyou():
    return render_template('thankyou.html')


def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database:
        name = data["fullName"]
        email = data["email"]
        message = data["msg"]
        csv_writer = csv.writer(
            database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name, email, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'Did not save to database'
    else:
        return 'something went wrong. Try again.'
