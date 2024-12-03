from flask import Flask, render_template, redirect, url_for, request, flash, session
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import mysql.connector
import requests
from config import API_KEY, BASE_URL, DB_HOST, DB_USER, DB_PASSWORD, DB_NAME, SECRET_KEY
from setup_server import setup_database
from datetime import timedelta

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30) 

login_manager = LoginManager(app)
login_manager.login_view = "login"

def get_db_connection():
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

@app.route('/')
def home():
    weather_data = {} 
    return render_template("index.html", weather_data=weather_data)

app = Flask(__name__)
app.secret_key = "your_secret_key"

# Initialize LoginManager
login_manager = LoginManager(app)

class User(UserMixin):
    def __init__(self, id):
        self.id = id

# User loader function
@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

class User(UserMixin):
    def __init__(self, id, username, email):
        self.id = id
        self.username = username
        self.email = email

    @staticmethod
    def get(user_id):
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
        user_data = cursor.fetchone()
        cursor.close()
        connection.close()

        if user_data:
            return User(user_data["id"], user_data["username"], user_data["email"])
        return None

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        hashed_password = generate_password_hash(password, method='sha256')

        connection = get_db_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("INSERT INTO users (username, email, password_hash) VALUES (%s, %s, %s)",
                           (username, email, hashed_password))
            connection.commit()
            flash("User successfully created!", "success")
            return redirect(url_for("login"))
        except mysql.connector.Error as err:
            flash(f"Error: {err}", "danger")
        finally:
            cursor.close()
            connection.close()

    return render_template("signup.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        remember = request.form.get("remember")

        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        user_data = cursor.fetchone()
        cursor.close()
        connection.close()

        if user_data and check_password_hash(user_data["password_hash"], password):
            user = User(user_data["id"], user_data["username"], user_data["email"])
            login_user(user, remember=remember)
            return redirect(url_for("profile"))
        else:
            flash("Invalid credentials", "danger")

    return render_template("login.html")

@app.route("/profile")
@login_required
def profile():
    return render_template("profile.html", user=current_user)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))

@app.route("/", methods=["GET", "POST"])
def home():
    weather_data = None
    if request.method == "POST":
        city = request.form["city"]
        url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            weather_data = response.json()
        else:
            weather_data = None
    return render_template("index.html", weather_data=weather_data)

if __name__ == "__main__":
    try:
        print("Setting up the database...")
        setup_database()
        print("Database setup complete. Starting the app...")
    except Exception as e:
        print(f"Error during setup: {e}")
        exit(1)
    
    app.run(debug=True)
