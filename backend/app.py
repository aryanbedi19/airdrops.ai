from flask import Flask
from flask_migrate import Migrate
from routes import main
from config import Config
from models import db
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(main)

if __name__ == "__main__":
    app.run(debug=True)
