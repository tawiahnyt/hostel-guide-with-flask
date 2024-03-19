from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from hostels import db, ayensu_hostels_data, kwaprow_hostels_data, science_hostels_data, shatta_wale_hostels_data

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hostels.db'  # Use the correct database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
