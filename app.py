from flask import Flask
from flask import render_template, request
from config import Config
from database.db import db
from routes.auth_routes import auth
from flask import session
from utils.decorators import login_required
from models.user_model import User

app = Flask(__name__)

app.config.from_object(Config)
db.init_app(app)

app.register_blueprint(auth)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/profile')
@login_required
def profile():

    user = User.query.get(session['user_id'])

    return render_template('profile.html', user=user)

with app.app_context():
    db.create_all()

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)