from flask import Flask, render_template, redirect, url_for
import csv
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
bootstrap = Bootstrap(app)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/hostel-sections', methods=["GET", "POST"])
def hostel_sections():
    return render_template("hostel-sections.html")

@app.route('/hostel-sections/ayensu-hostels/', methods=["GET", "POST"])
def ayensu_hostels():
    with open('data/ayensu-hostels-data.csv') as csv_file:
        csv_data = csv.reader(csv_file)
        hostels = []
        for row in csv_data:
            hostels.append(row)

    return render_template("ayensu-hostel.html", hostels=hostels)

@app.route('/hostel-sections/shatta-wale-hostels/', methods=["GET", "POST"])
def shatta_wale_hostels():
    with open('data/shatta-wale-hostels-data.csv') as csv_file:
        csv_data = csv.reader(csv_file)
        hostels = []
        for row in csv_data:
            hostels.append(row)

    return render_template("shatta-wale-hostel.html", hostels=hostels)

@app.route('/hostel-sections/kwaprow-hostels/', methods=["GET", "POST"])
def kwaprow_hostels():
    with open('data/kwaprow-hostels-data.csv') as csv_file:
        csv_data = csv.reader(csv_file)
        hostels = []
        for row in csv_data:
            hostels.append(row)

    return render_template("kwapro-hostel.html", hostels=hostels)

@app.route('/hostel-sections/science-hostels/', methods=["GET", "POST"])
def science_hostels():
    with open('data/science-hostels-data.csv') as csv_file:
        csv_data = csv.reader(csv_file)
        hostels = []
        for row in csv_data:
            hostels.append(row)

    return render_template("science-hostel.html", hostels=hostels)

@app.route('/hostel-sections/<hostel_name>/hostel-details/<name>', methods=["GET", "POST"])
def hostel_details(hostel_name, name):
    return render_template("hostel-details.html", hostel_name=hostel_name, name=name)

if __name__ == '__main__':
    app.run()


