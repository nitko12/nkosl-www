from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

nkosl_app = Flask(__name__)
nkosl_app.config['SECRET_KEY'] = 'du_bist_mein_sofa'
nkosl_app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://nkosl:nkosl@10.0.3.25/nkosl"
nkosl_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(nkosl_app)
migrate = Migrate(nkosl_app, db)

from app import routes
