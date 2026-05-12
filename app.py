from flask import Flask
from flask import render_template
from config import Config
from database.db import db
from routes.auth_routes import auth

app = Flask(__name__)

app.config.from_object(Config)
db.init_app(app)

app.register_blueprint(auth)

@app.route('/')
def home():
    return render_template('index.html')

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)