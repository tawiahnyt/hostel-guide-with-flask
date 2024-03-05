from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
import csv

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/authentication')
def auth():
    return render_template("auth.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = request.form
        email = data['email']
        # Check if a user with the same email already exists
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash("You've already signed up with that email, please login instead.")
            return render_template("login.html")
        # Hash and salt the password
        hashed_password = generate_password_hash(data['password'], salt_length=8)
        new_user = User(
            email=email,
            password=hashed_password,
            name=data['name']
        )
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect(url_for('hostel_sections'))
    return render_template("register.html", logged_in=current_user.is_authenticated)


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        # Email doesn't exist or password incorrect.
        if not user:
            flash("That email does not exist, please try again.")
            return redirect(url_for('login'))
        elif not check_password_hash(user.password, password):
            flash('Password incorrect, please try again.')
            return redirect(url_for('login'))
        else:
            login_user(user)
            return redirect(url_for('hostel_sections'))
    return render_template("login.html", logged_in=current_user.is_authenticated)

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


